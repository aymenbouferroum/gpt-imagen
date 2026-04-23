# Capabilities

GPT Imagen is deliberately GPT Image 2-first on the direct OpenAI API path.

## Why GPT Image 2 is the default

- OpenAI positions GPT Image 2 as its state-of-the-art image generation model
- the official image guide presents it as the model for high-quality generation and editing
- it fits the exact workflows this plugin targets: frontend concepts, game assets, product imagery, and conceptual technical visuals

## What GPT Imagen is good at

- product hero images
- landing page and dashboard mockups
- concept art and game asset ideation
- marketing visuals and social assets
- paper-cover and pipeline concept figures
- background removal and reference-driven edits

## What it is not good at

- deterministic SVG output
- exact typography-heavy posters
- pixel-perfect interface screenshots with exact production copy
- final academic charts derived from measured data
- transparent-background generation on the direct `gpt-image-2` API path

## Provider matrix

| Provider | Best for | Notes |
|---|---|---|
| Codex subscription | zero-setup image generation from Claude when Codex is already logged in | Uses `codex exec` and the built-in image workflow |
| OpenAI Images API | explicit GPT Image 2-first execution, controlled model selection, mask-based edits | Defaults to `gpt-image-2` and gives direct control over output pathing |

## Practical reading of the model choice

This plugin is not trying to be neutral between image models.

The default assumption is:

- if you want the direct API path, you probably want GPT Image 2
- if you want a convenience path through a local Codex setup, the plugin still supports that
- if you want a different GPT Image model, you can override it, but the repo copy and defaults are optimized around GPT Image 2
