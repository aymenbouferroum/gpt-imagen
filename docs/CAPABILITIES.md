# Capabilities

## What GPT Imagen is built for

- Product hero images and marketing visuals
- Landing page and dashboard mockups
- Concept art and game asset ideation
- Paper-cover and pipeline concept figures
- Background removal and reference-driven image edits

## What it is not built for

- Deterministic SVG or vector output
- Exact typography-heavy designs
- Pixel-perfect interface screenshots with production copy
- Final academic charts and plots from measured data
- Transparent-background generation on the direct `gpt-image-2` API path

## Provider comparison

| | OpenAI Images API | Codex CLI |
|---|---|---|
| **Model** | `gpt-image-2` (configurable) | Set by Codex (configurable via `codex_model`) |
| **Edit support** | Full (mask-based edits) | Prompt-driven |
| **Transparency** | Not supported on `gpt-image-2` | Depends on Codex model |
| **Setup** | API key required | `codex login` required |
| **Best for** | Controlled generation, edits, specific model selection | Quick generation without API key management |

## GPT Image 2 reference links

- [GPT Image 2 model page](https://platform.openai.com/docs/models/gpt-image-2)
- [Image generation guide](https://platform.openai.com/docs/guides/image-generation)
- [Image generation tool guide](https://platform.openai.com/docs/guides/tools-image-generation)
