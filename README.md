# Visual Forge

Visual Forge is a Claude Code plugin marketplace and flagship plugin for serious image generation workflows.

![Visual Forge logo](assets/branding/visual-forge-logo.png)

It gives Claude a reliable way to create and edit visuals for:

- frontend and product design
- landing pages and dashboard mockups
- game assets and concept art
- research and paper-cover visuals
- product cutouts and visual asset generation

It supports two execution paths:

- local Codex subscription through `codex exec`
- OpenAI Images API through the user's own API key

![Visual Forge header](assets/branding/visual-forge-header.png)

## Why this exists

Most image skills stop at "write a better prompt." That is not enough.

Visual Forge gives Claude:

- capability-aware provider routing
- reusable visual prompt scaffolds
- practical workflows for UI, games, assets, and paper visuals
- consistent output saving behavior
- a marketplace-friendly install story

## Install

### Marketplace install

```bash
claude plugin marketplace add YOUR_GITHUB_USERNAME/visual-forge-marketplace
claude plugin install visual-forge-studio@visual-forge
```

### Local dev install

```bash
claude plugin marketplace add .
claude plugin install visual-forge-studio@visual-forge
```

### Direct plugin dev mode

```bash
claude --plugin-dir ./plugins/visual-forge-studio
```

More detail: [docs/INSTALL.md](docs/INSTALL.md)

## Included skills

- `/visual-forge`
  General-purpose image generation and editing workflow
- `/frontend-mockup`
  UI and product-visual workflows for sites, apps, dashboards, and launch assets
- `/game-asset-lab`
  Sprites, props, icons, promo art, and stylized game visual assets
- `/paper-figure-visual`
  Conceptual research figures, pipeline visuals, and illustration-style paper assets
- `/image-edit-studio`
  Background cleanup, restyling, object-focused edits, and reference-driven changes

## Example gallery

### Frontend mockup reference

![Frontend example](assets/examples/frontend-mockup-example.png)

### Game asset reference

![Game asset example](assets/examples/game-asset-example.png)

### Paper figure reference

![Paper figure example](assets/examples/paper-figure-example.png)

### Product asset reference

![Product asset example](assets/examples/product-asset-example.png)

## Provider model

Visual Forge supports two ways to run:

### 1. Codex subscription

If `codex` is installed and logged in, the plugin can route image tasks through the local Codex CLI. This is the fastest path for users who already have a Codex-capable setup.

### 2. OpenAI API key

If the user provides `openai_api_key` in plugin configuration, the plugin can call the OpenAI Images API directly. The default image model is configurable and ships set to `gpt-image-2`.

The plugin prefers `auto` mode by default:

1. use Codex if available and logged in
2. otherwise use the OpenAI API if configured
3. otherwise fail with a clear setup message

## Repo structure

```text
visual-forge-marketplace/
├── .claude-plugin/marketplace.json
├── docs/
├── assets/
└── plugins/
    └── visual-forge-studio/
        ├── .claude-plugin/plugin.json
        ├── bin/visual-forge
        ├── scripts/vforge.py
        ├── references/
        └── skills/
```

## Safety and realism

Visual Forge is optimized for practical creative work, not hype:

- it does not promise exact typography or perfect layout geometry
- it distinguishes concept figures from numeric charts
- it keeps vector-native work out of the image pipeline
- it saves generated files predictably so users can keep working

## Documentation

- [Install](docs/INSTALL.md)
- [Tutorial](docs/TUTORIAL.md)
- [Capabilities](docs/CAPABILITIES.md)
- [Contributing](CONTRIBUTING.md)
- [Acknowledgments](ACKNOWLEDGMENTS.md)

## License

MIT
