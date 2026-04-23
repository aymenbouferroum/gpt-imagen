---
name: game-asset-lab
description: Generate game visual assets such as icons, props, key art, item sheets, stylized environments, and concept art. Use when the user is doing game ideation or asset creation and needs actual image outputs.
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
argument-hint: "<asset brief>"
---

# Game Asset Lab

Use this skill for practical game-art generation work.

The `gpt-imagen` binary handles provider detection automatically. Do not check for API keys or Codex login status yourself. Always run the binary and let it decide. Never refuse to run it because you think a provider is missing.

## Ask internally

- Is this an icon, prop, environment, character concept, splash art, or sprite-style sheet?
- Does the user need transparency?
- Is this a one-off asset or part of a consistent set?
- Does the style need to be pixel art, painterly, 3D stylized, cozy, dark fantasy, sci-fi, or something else?

## Execution defaults

- for icons and props, prefer isolated compositions and transparent backgrounds when useful
- for sets, explicitly request a shared style family
- for sprite-like outputs, say so directly instead of saying "game asset" generically

