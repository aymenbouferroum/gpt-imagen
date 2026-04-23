# Install

## Install from GitHub

```bash
claude plugin marketplace add aymenbouferroum/gpt-imagen
claude plugin install gpt-imagen@gpt-imagen
```

By default, Claude installs plugins at `user` scope, which makes them available globally across projects.

## Install from a local checkout

```bash
claude plugin marketplace add .
claude plugin install gpt-imagen@gpt-imagen
```

Run both commands from the repository root.

## Direct development mode

```bash
claude --plugin-dir ./plugins/gpt-imagen
```

## Provider setup

GPT Imagen supports two execution paths:

1. Codex subscription path
   Requirement: `codex` installed and `codex login status` succeeds.

2. OpenAI API path
   Requirement: an OpenAI API key supplied through plugin configuration or `OPENAI_API_KEY`.

The direct API path is GPT Image 2-first and defaults to `gpt-image-2`.

On plugin enable, configure:

- `provider_mode`: `auto`, `codex`, or `openai`
- `openai_api_key`: optional, sensitive
- `openai_image_model`: defaults to `gpt-image-2`
- `codex_model`: defaults to `gpt-5.4`

`auto` prefers Codex when available, then falls back to the API path.

If you stay on the direct API default, note that `gpt-image-2` currently does not support transparent backgrounds. Use `auto` or `opaque`, or pick another GPT Image model when transparency is required.

## Configuration reference

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `provider_mode` | string | `auto` | Provider selection: `auto`, `codex`, or `openai` |
| `openai_api_key` | string (sensitive) | — | OpenAI API key for the direct API path |
| `openai_image_model` | string | `gpt-image-2` | Image model used on the OpenAI path |
| `openai_base_url` | string | `https://api.openai.com/v1` | Base URL for the Images API |
| `codex_model` | string | `gpt-5.4` | Model passed to `codex exec` |
| `default_output_dir` | directory | (workspace) | Default directory for saved images; leave blank for current workspace |
