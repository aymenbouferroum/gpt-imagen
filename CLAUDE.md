# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

GPT Imagen is a Claude Code plugin marketplace shipping a single plugin (`gpt-imagen`) for image generation and editing workflows. It routes requests to either a local Codex CLI or the OpenAI Images API. The entire plugin is stdlib-only Python 3 — no external dependencies, no package manager, no build step.

## Development Commands

```bash
# Validate plugin structure
claude plugin validate .

# Test plugin directly (dev mode)
claude --plugin-dir ./plugins/gpt-imagen

# Test full marketplace install flow
claude plugin marketplace add .
claude plugin install gpt-imagen@gpt-imagen

# Release: bump version in plugins/gpt-imagen/.claude-plugin/plugin.json, then
claude plugin tag ./plugins/gpt-imagen

# Run the script directly (outside Claude) for manual testing
python3 plugins/gpt-imagen/scripts/vforge.py "a red cube on white background" --out /tmp/test.png
# or via the bash wrapper:
plugins/gpt-imagen/bin/gpt-imagen "a red cube" --out /tmp/test.png
```

There are no test suites, linters, or CI pipelines configured.

### CLI Interface (`vforge.py`)

The script accepts these arguments — this is the contract between the SKILL.md files and the execution engine:

```
vforge.py [prompt...] [--provider auto|codex|openai] [--image PATH]...
          [--mask PATH] [--out PATH] [--model MODEL]
          [--size auto|1024x1024|1024x1536|1536x1024]
          [--quality auto|low|medium|high]
          [--background auto|transparent|opaque]
          [--format png|jpeg|webp] [--input-fidelity low|high]
```

Prompt can also be piped via stdin. Multiple `--image` flags attach reference/edit images. When any `--image` or `--mask` is present, the OpenAI path switches from `/images/generations` to `/images/edits`.

## Architecture

### Provider Router (`plugins/gpt-imagen/scripts/vforge.py`)

Single-file Python script (~328 lines) that serves as the entire execution engine. The bash wrapper at `bin/gpt-imagen` delegates directly to it.

**Provider selection** (`choose_provider`): In `auto` mode (default), tries Codex first (checks `codex login status`), falls back to OpenAI API if a key is configured, fails with a setup message otherwise.

**Codex path** (`run_codex`): Shells out to `codex exec --full-auto`, then locates the generated image either from Codex's stdout or by scanning `~/.codex/generated_images/` for the newest file after the run started.

**OpenAI path** (`run_openai`): Makes direct HTTP requests via `urllib` — JSON POST to `/images/generations` for new images, multipart form-data POST to `/images/edits` when input images or masks are provided. No SDK used.

**Configuration** (`plugin_option`): Reads `CLAUDE_PLUGIN_OPTION_*` environment variables set by the Claude plugin system (e.g. `CLAUDE_PLUGIN_OPTION_OPENAI_API_KEY`). The API key also falls back to the `OPENAI_API_KEY` env var. The `userConfig` schema in `plugin.json` defines which options exist and their defaults — that schema is the source of truth for configurable options.

### Plugin Structure

```
plugins/gpt-imagen/
├── .claude-plugin/plugin.json   # Plugin metadata + userConfig schema
├── bin/gpt-imagen              # Bash entry point → vforge.py
├── scripts/vforge.py            # Provider router (the only code file)
├── references/                  # Prompt patterns + provider comparison docs
│   ├── prompt-patterns.md
│   └── provider-matrix.md
└── skills/                      # Five SKILL.md files defining Claude workflows
    ├── gpt-imagen/             # General-purpose generation/editing
    ├── frontend-mockup/         # UI/product visuals
    ├── game-asset-lab/          # Game sprites, icons, concept art
    ├── paper-figure-visual/     # Research figures and diagrams
    └── image-edit-studio/       # Background removal, restyling, edits
```

### Marketplace Layer

`.claude-plugin/marketplace.json` at repo root registers the marketplace and points to the single plugin. The plugin's own `.claude-plugin/plugin.json` defines user-configurable options (provider mode, API keys, models, output directory).

## Key Design Decisions

- **Zero external dependencies**: stdlib-only Python. HTTP via `urllib`, multipart encoding hand-rolled, no OpenAI SDK.
- **Honest about limits**: Skills explicitly disclaim exact typography, precise layout geometry, and vector determinism. Don't oversell image generation capabilities.
- **Predictable output**: Default filename is `gpt-imagen-YYYYMMDD-HHMMSS.png` in the working directory. Parent directories are created automatically.
- **Skills are prompt scaffolds, not code**: Each skill under `skills/` is a SKILL.md file that instructs Claude how to invoke `bin/gpt-imagen` with the right arguments — they contain no executable code.
- **GPT Image 2 transparent background guard**: `vforge.py` hard-fails if `model=gpt-image-2` and `background=transparent` — this is an upstream API limitation enforced in code rather than left to a cryptic API error.
