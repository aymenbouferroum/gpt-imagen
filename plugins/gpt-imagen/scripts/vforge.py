#!/usr/bin/env python3
"""Provider-aware image generation router for the GPT Imagen Claude plugin."""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import uuid
from typing import NoReturn


IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}
PATH_RE = re.compile(r"(/[^\s\"']+\.(?:png|jpg|jpeg|webp))", re.IGNORECASE)


def plugin_option(name: str, default: str | None = None) -> str | None:
    key = f"CLAUDE_PLUGIN_OPTION_{name.upper()}"
    value = os.environ.get(key)
    return value if value not in (None, "") else default


def fail(message: str, code: int = 1) -> NoReturn:
    print(f"gpt-imagen: {message}", file=sys.stderr)
    raise SystemExit(code)


def load_prompt(prompt_parts: list[str]) -> str:
    if prompt_parts == ["-"]:
        prompt = sys.stdin.read().strip()
    elif prompt_parts:
        prompt = " ".join(prompt_parts).strip()
    else:
        prompt = sys.stdin.read().strip()
    if not prompt:
        fail("no prompt provided")
    return prompt


def resolve_output_path(output_path: str | None, default_dir: str | None) -> pathlib.Path:
    if output_path:
        path = pathlib.Path(output_path).expanduser()
    else:
        base_dir = pathlib.Path(default_dir).expanduser() if default_dir else pathlib.Path.cwd()
        stamp = time.strftime("%Y%m%d-%H%M%S")
        path = base_dir / f"gpt-imagen-{stamp}.png"
    if not path.is_absolute():
        path = pathlib.Path.cwd() / path
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def codex_available() -> bool:
    return shutil.which("codex") is not None


def codex_logged_in() -> bool:
    if not codex_available():
        return False
    result = subprocess.run(
        ["codex", "login", "status"],
        capture_output=True,
        text=True,
        check=False,
    )
    text = (result.stdout + result.stderr).strip()
    return result.returncode == 0 and "Logged in" in text


def newest_codex_image(after_ts: float) -> pathlib.Path | None:
    root = pathlib.Path.home() / ".codex" / "generated_images"
    if not root.exists():
        return None
    candidates: list[tuple[float, pathlib.Path]] = []
    for path in root.rglob("*"):
        if path.suffix.lower() in IMAGE_SUFFIXES and path.is_file():
            try:
                mtime = path.stat().st_mtime
            except OSError:
                continue
            if mtime >= after_ts - 2:
                candidates.append((mtime, path))
    if not candidates:
        return None
    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0][1]


def build_codex_prompt(user_prompt: str, image_count: int) -> str:
    image_clause = (
        "Treat attached images as edit targets or reference images as appropriate."
        if image_count
        else "No input images are attached."
    )
    return (
        "Use the built-in image generation workflow.\n"
        "Generate one strong final image that satisfies the user request.\n"
        f"{image_clause}\n"
        "After generation, respond with the absolute path to the final saved image only.\n\n"
        "User request:\n"
        f"{user_prompt}\n"
    )


def run_codex(prompt: str, images: list[str], output_path: pathlib.Path, codex_model: str | None) -> pathlib.Path:
    if not codex_available():
        fail("codex CLI is not installed")
    if not codex_logged_in():
        fail("codex is not logged in. Run `codex login` or switch to the OpenAI API provider.")

    started = time.time()
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".txt") as handle:
        result_file = pathlib.Path(handle.name)

    cmd = ["codex", "exec", "--full-auto", "-C", str(pathlib.Path.cwd()), "-o", str(result_file)]
    if codex_model:
        cmd.extend(["-m", codex_model])
    for image in images:
        cmd.extend(["--image", image])
    cmd.append("-")

    try:
        proc = subprocess.run(
            cmd,
            input=build_codex_prompt(prompt, len(images)),
            text=True,
            check=False,
        )

        if proc.returncode != 0:
            fail("codex image generation failed")

        returned_text = result_file.read_text(encoding="utf-8", errors="ignore").strip() if result_file.exists() else ""
        matched = PATH_RE.search(returned_text)
        source = pathlib.Path(matched.group(1)) if matched else newest_codex_image(started)
        if not source or not source.exists():
            fail("could not locate the generated Codex image")

        shutil.copy2(source, output_path)
        return output_path
    finally:
        result_file.unlink(missing_ok=True)


def encode_multipart_formdata(fields: list[tuple[str, str]], files: list[tuple[str, pathlib.Path]]) -> tuple[bytes, str]:
    boundary = f"----GptImagen{uuid.uuid4().hex}"
    chunks: list[bytes] = []

    for name, value in fields:
        chunks.append(f"--{boundary}\r\n".encode())
        chunks.append(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode())
        chunks.append(value.encode())
        chunks.append(b"\r\n")

    for name, path in files:
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        chunks.append(f"--{boundary}\r\n".encode())
        chunks.append(
            f'Content-Disposition: form-data; name="{name}"; filename="{path.name}"\r\n'.encode()
        )
        chunks.append(f"Content-Type: {mime}\r\n\r\n".encode())
        chunks.append(path.read_bytes())
        chunks.append(b"\r\n")

    chunks.append(f"--{boundary}--\r\n".encode())
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


def openai_headers(api_key: str, content_type: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": content_type,
    }


def run_openai(
    prompt: str,
    images: list[str],
    mask: str | None,
    output_path: pathlib.Path,
    model: str,
    api_key: str,
    base_url: str,
    size: str | None,
    quality: str | None,
    background: str | None,
    output_format: str,
    input_fidelity: str | None,
) -> pathlib.Path:
    base_url = base_url.rstrip("/")
    if not api_key:
        fail("OpenAI API key is missing. Configure openai_api_key or set OPENAI_API_KEY.")
    if model == "gpt-image-2" and background == "transparent":
        fail("gpt-image-2 does not currently support transparent backgrounds on the direct API path. Use background=auto or opaque, or choose another GPT Image model.")

    if images or mask:
        url = f"{base_url}/images/edits"
        fields = [("model", model), ("prompt", prompt), ("output_format", output_format)]
        if size:
            fields.append(("size", size))
        if quality:
            fields.append(("quality", quality))
        if background:
            fields.append(("background", background))
        if input_fidelity and model != "gpt-image-2":
            fields.append(("input_fidelity", input_fidelity))
        files = [("image[]", pathlib.Path(image)) for image in images]
        if mask:
            files.append(("mask", pathlib.Path(mask)))
        body, content_type = encode_multipart_formdata(fields, files)
        req = urllib.request.Request(url, data=body, headers=openai_headers(api_key, content_type), method="POST")
    else:
        url = f"{base_url}/images/generations"
        payload = {
            "model": model,
            "prompt": prompt,
            "output_format": output_format,
        }
        if size:
            payload["size"] = size
        if quality:
            payload["quality"] = quality
        if background:
            payload["background"] = background
        body = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=body,
            headers=openai_headers(api_key, "application/json"),
            method="POST",
        )

    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="ignore")
        fail(f"OpenAI API request failed ({exc.code}): {error_body}")
    except urllib.error.URLError as exc:
        fail(f"OpenAI API request failed: {exc}")

    try:
        image_b64 = payload["data"][0]["b64_json"]
    except (KeyError, IndexError, TypeError):
        fail("OpenAI API response did not contain image data")

    output_path.write_bytes(base64.b64decode(image_b64))
    return output_path


def choose_provider(requested: str, has_api_key: bool) -> str:
    normalized = (requested or "auto").strip().lower()
    if normalized not in {"auto", "codex", "openai"}:
        fail("provider must be auto, codex, or openai")
    if normalized == "codex":
        return "codex"
    if normalized == "openai":
        return "openai"
    if codex_logged_in():
        return "codex"
    if has_api_key:
        return "openai"
    fail("no provider available. Log into Codex or configure an OpenAI API key.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="GPT Imagen image router")
    parser.add_argument("prompt", nargs="*", help="Prompt text. If omitted, prompt is read from stdin.")
    parser.add_argument("--provider", default=plugin_option("provider_mode", "auto"))
    parser.add_argument("--image", action="append", default=[], help="Input image path. Repeat for multiple images.")
    parser.add_argument("--mask", help="Optional mask image for the OpenAI API edit flow.")
    parser.add_argument("--out", help="Output image path.")
    parser.add_argument("--model", help="Override the image model.")
    parser.add_argument("--size", default="auto", choices=["auto", "1024x1024", "1024x1536", "1536x1024"])
    parser.add_argument("--quality", default="auto", choices=["auto", "low", "medium", "high"])
    parser.add_argument("--background", default="auto", choices=["auto", "transparent", "opaque"])
    parser.add_argument("--format", default="png", choices=["png", "jpeg", "webp"])
    parser.add_argument("--input-fidelity", default="high", choices=["low", "high"])
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    prompt = load_prompt(args.prompt)
    default_output_dir = plugin_option("default_output_dir")
    output_path = resolve_output_path(args.out, default_output_dir)
    openai_api_key = plugin_option("openai_api_key") or os.environ.get("OPENAI_API_KEY")
    provider = choose_provider(args.provider, bool(openai_api_key))

    if provider == "codex":
        codex_model = args.model or plugin_option("codex_model", "gpt-5.4")
        final_path = run_codex(prompt, args.image, output_path, codex_model)
    else:
        openai_model = args.model or plugin_option("openai_image_model", "gpt-image-2") or "gpt-image-2"
        openai_base_url = plugin_option("openai_base_url", "https://api.openai.com/v1")
        final_path = run_openai(
            prompt=prompt,
            images=args.image,
            mask=args.mask,
            output_path=output_path,
            model=openai_model,
            api_key=openai_api_key or "",
            base_url=openai_base_url or "https://api.openai.com/v1",
            size=args.size,
            quality=args.quality,
            background=args.background,
            output_format=args.format,
            input_fidelity=args.input_fidelity,
        )

    print(str(final_path.resolve()))


if __name__ == "__main__":
    main()
