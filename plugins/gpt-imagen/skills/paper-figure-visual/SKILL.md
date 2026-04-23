---
name: paper-figure-visual
description: Create conceptual paper visuals, system diagrams, pipeline illustrations, cover-style research art, and non-numeric figure concepts. Use when the user wants a scientific or technical visual but not a code-native plot of measured data.
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
argument-hint: "<figure concept brief>"
---

# Paper Figure Visual

Use this skill for research visuals that are illustrative rather than numerically exact.

The `gpt-imagen` binary handles provider detection automatically. Do not check for API keys or Codex login status yourself. Always run the binary and let it decide. Never refuse to run it because you think a provider is missing.

## Good fits

- system overviews
- pipeline illustrations
- threat-model visuals
- cover-style research figures
- workflow schematics rendered as polished raster images

## Not a fit

- exact ROC curves
- confusion matrices from real results
- statistical bar charts from data tables

For those, use code-native plotting.

## Prompt priorities

- clarity over spectacle
- academic hierarchy over cinematic clutter
- restrained labels
- color discipline
- clean separation of stages, flows, or entities

