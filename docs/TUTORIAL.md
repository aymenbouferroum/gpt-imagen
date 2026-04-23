# Tutorial

## 1. Frontend mockup

Prompt Claude with:

```text
/frontend-mockup Create a premium landing-page hero for a developer tool that explains observability for AI agents. Keep it bright, editorial, and product-oriented.
```

Claude should:

- refine the prompt into a visual spec
- call the bundled `visual-forge` binary
- save the result into your workspace if you ask for a file path

## 2. Game asset

```text
/game-asset-lab Create a 2D fantasy inventory icon set for a potion, iron key, compass, and rune scroll on transparent backgrounds.
```

Use this when you want:

- item icons
- environment props
- promo key art
- sprite-style assets

## 3. Paper figure visual

```text
/paper-figure-visual Create a conceptual security-paper figure showing a two-stage edge-to-cloud detection pipeline with anomaly gating and zero-day handling.
```

This skill is for:

- conceptual figures
- research illustrations
- cover-style diagrams
- pipeline overview visuals

It is not for plotting measured data. Use code-native plotting for final numeric charts.

## 4. Image edit

```text
/image-edit-studio Clean up this product shot, remove the busy background, keep the device shape unchanged, and output a transparent PNG.
```

If you need highly controlled masked edits, prefer the OpenAI API path and include a mask.

