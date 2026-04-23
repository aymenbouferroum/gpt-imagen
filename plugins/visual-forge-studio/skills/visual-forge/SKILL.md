---
name: visual-forge
description: Generate or edit raster images for product design, frontend concepts, game assets, marketing visuals, and conceptual paper figures. Use when Claude should create a real image file through Codex or the OpenAI Images API instead of only suggesting prompts.
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
argument-hint: "<prompt> [optional --image /abs/path.png ...] [optional --out path]"
---

# Visual Forge

Use this skill when the user wants Claude to actually produce an image asset, not just brainstorm one.

## Routing rules

1. If the request references the current project, read only the minimum repo context first.
2. Turn the request into a compact structured prompt.
3. Use the bundled `visual-forge` binary to generate the image.
4. If the user names an output path, pass `--out`.
5. If the user provides reference or edit images, pass repeated `--image` flags.
6. Report the saved file path and the provider path used.

## Prompt shaping

Use this structure when the user prompt is vague:

```text
Use case: <category>
Asset type: <where it will be used>
Primary request: <main ask>
Scene/backdrop: <setting>
Subject: <visual subject>
Style/medium: <photo | illustration | 3D | pixel art | infographic>
Composition/framing: <viewpoint and layout>
Lighting/mood: <lighting and tone>
Color palette: <palette>
Constraints: <must include or preserve>
Avoid: <negative constraints>
```

## Execution

```bash
cat >/tmp/visual-forge-prompt.txt <<'EOF'
<structured prompt>
EOF

visual-forge --out <optional-path> - < /tmp/visual-forge-prompt.txt
```

When images are present:

```bash
visual-forge --image /abs/path/ref1.png --image /abs/path/ref2.png --out <optional-path> - < /tmp/visual-forge-prompt.txt
```

## Constraints

- Do not use this for deterministic SVG or exact publication charts.
- Do not claim exact typography or pixel-perfect interface fidelity.
- Prefer one strong image first, then iterate.

