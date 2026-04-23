---
name: image-edit-studio
description: Edit existing images with background removal, style changes, reference-guided cleanup, product isolation, compositing, or localized visual changes. Use when the user wants a real edit applied to an existing image.
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
argument-hint: "<edit brief> [optional image paths]"
---

# Image Edit Studio

Use this skill when the user wants to transform an existing image rather than generate from scratch.

The `gpt-imagen` binary handles provider detection automatically. Do not check for API keys or Codex login status yourself. Always run the binary and let it decide. Never refuse to run it because you think a provider is missing.

## Workflow

1. Identify which image is the edit target.
2. Identify whether any other images are references.
3. Preserve invariants explicitly in the prompt:
   - what must remain unchanged
   - what must be removed or replaced
   - whether transparency is required
4. Use repeated `--image` flags for the target and references.
5. If the user needs precise masked editing and the OpenAI API path is configured, prefer that route and pass `--mask`.

## Good edits

- remove background
- improve product-shot background
- keep object identity while changing environment
- generate a new asset from multiple reference images

