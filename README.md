# GPT Imagen

GPT Imagen is a Claude Code plugin marketplace built around one core idea: make Claude Code feel like Claude Code merged with GPT Image 2.

![GPT Imagen logo](assets/branding/gpt-imagen-logo.png)

![Claude Code + GPT Image 2 hero](assets/branding/gpt-imagen-claude-code-gpt-image-2-header.png)

GPT Imagen is intentionally GPT Image 2-first on the direct OpenAI API path, and it keeps a Codex-powered path for users who want Claude to drive image workflows without wiring an API key first.

It gives Claude a reliable way to create and edit visuals for:

- frontend and product design
- landing pages and dashboard mockups
- game assets and concept art
- research and paper-cover visuals
- product cutouts and visual asset generation

It supports two execution paths:

- local Codex subscription through `codex exec`
- OpenAI Images API through the user's own API key

## Why this exists

Most image skills stop at "write a better prompt." That is not enough.

GPT Imagen gives Claude:

- capability-aware provider routing
- reusable visual prompt scaffolds
- practical workflows for UI, games, assets, and paper visuals
- consistent output saving behavior
- a marketplace-friendly install story

## Why GPT Image 2

The main point of this repo is GPT Image 2.

OpenAI currently documents GPT Image 2 as its state-of-the-art image generation model, and specifically describes it as the model for fast, high-quality image generation and editing with flexible image sizes and high-fidelity image inputs. That is the reason this plugin is opinionated around GPT Image 2 instead of treating all image models as interchangeable.

Claude Code is strong at orchestration, repo context, task decomposition, and prompt refinement. GPT Image 2 is strong at turning those structured intents into actual images. GPT Imagen exists to join those two strengths into one workflow:

- Claude Code reads the repo and understands what the user is building
- Claude Code turns vague requests into a visual spec
- GPT Image 2 handles generation and editing on the direct API path
- Codex remains available as a no-key convenience path for users who already work that way

This means the repo is not trying to be a generic wrapper for every image model. It is deliberately optimized around GPT Image 2 as the primary default.

## GPT Image 2 strengths this repo is built for

- High-end generation and editing in one model, instead of splitting the workflow across weak specialized wrappers
- Flexible image sizes, including square, portrait, landscape, and larger resolutions on the direct API path
- High-fidelity image inputs by default for edit and reference-image workflows
- Strong fit for UI concepts, game assets, product renders, and conceptual research figures
- Clean pairing with a reasoning model or agent layer that can revise prompts before generation

## What I will not claim

This repo is intentionally pro GPT Image 2, but it does not make unsupported leaderboard claims.

- It does not claim GPT Image 2 "beats everyone" as a factual benchmark statement
- It does not pretend image generation is perfect at exact typography or vector-like determinism
- It does not hide GPT Image 2 limitations, such as the current lack of transparent background support on the direct API path

## Official OpenAI references

- GPT Image 2 model page: <https://developers.openai.com/api/docs/models/gpt-image-2>
- Image generation guide: <https://developers.openai.com/api/docs/guides/image-generation>
- Image generation tool guide: <https://developers.openai.com/api/docs/guides/tools-image-generation>

## Install

### Marketplace install

```bash
claude plugin marketplace add aymenbouferroum/gpt-imagen-marketplace
claude plugin install gpt-imagen@gpt-imagen
```

### Local dev install

```bash
claude plugin marketplace add .
claude plugin install gpt-imagen@gpt-imagen
```

### Direct plugin dev mode

```bash
claude --plugin-dir ./plugins/gpt-imagen
```

More detail: [docs/INSTALL.md](docs/INSTALL.md)

## Included skills

- `/gpt-imagen`
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

GPT Imagen supports two ways to run:

### 1. Codex subscription

If `codex` is installed and logged in, the plugin can route image tasks through the local Codex CLI. This is the fastest path for users who already have a Codex-capable setup.

### 2. OpenAI API key

If the user provides `openai_api_key` in plugin configuration, the plugin can call the OpenAI Images API directly. The default image model is configurable and ships set to `gpt-image-2`.

This is the path that makes the plugin explicitly GPT Image 2-first.

The plugin prefers `auto` mode by default:

1. use Codex if available and logged in
2. otherwise use the OpenAI API if configured
3. otherwise fail with a clear setup message

## Claude Code x GPT Image 2

The workflow this repository wants is simple:

1. Claude Code understands the project, product, paper, game, or design brief.
2. Claude Code structures the ask into a stronger visual prompt.
3. GPT Image 2 generates or edits the image.
4. Claude Code saves the result back into the working repo and keeps iterating.

OpenAI's image-generation tool docs also note that when using the image generation tool, a mainline model such as `gpt-5.4` can automatically revise the prompt for improved performance. That is exactly the kind of orchestration story this plugin leans into.

## Repo structure

```text
gpt-imagen-marketplace/
├── .claude-plugin/marketplace.json
├── docs/
├── assets/
└── plugins/
    └── gpt-imagen/
        ├── .claude-plugin/plugin.json
        ├── bin/gpt-imagen
        ├── scripts/vforge.py
        ├── references/
        └── skills/
```

## Safety and realism

GPT Imagen is optimized for practical creative work, not hype:

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
