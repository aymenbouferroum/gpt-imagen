# Install

## Add the marketplace from GitHub

```bash
claude plugin marketplace add YOUR_GITHUB_USERNAME/visual-forge-marketplace
claude plugin install visual-forge-studio@visual-forge
```

By default, Claude installs plugins at `user` scope, which makes them available globally across projects.

## Install from a local checkout

```bash
claude plugin marketplace add .
claude plugin install visual-forge-studio@visual-forge
```

Run both commands from the repository root.

## Direct development mode

```bash
claude --plugin-dir ./plugins/visual-forge-studio
```

## Provider setup

Visual Forge supports two execution paths:

1. Codex subscription path
   Requirement: `codex` installed and `codex login status` succeeds.

2. OpenAI API path
   Requirement: an OpenAI API key supplied through plugin configuration or `OPENAI_API_KEY`.

On plugin enable, configure:

- `provider_mode`: `auto`, `codex`, or `openai`
- `openai_api_key`: optional, sensitive
- `openai_image_model`: defaults to `gpt-image-2`
- `codex_model`: defaults to `gpt-5.4`

`auto` prefers Codex when available, then falls back to the API path.
