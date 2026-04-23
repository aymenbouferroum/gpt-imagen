---
name: frontend-mockup
description: Create visual mockups for landing pages, product heroes, dashboards, mobile screens, app store creatives, and UI marketing shots. Use when the user wants a frontend concept image rather than production code.
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
argument-hint: "<product or UI brief>"
---

# Frontend Mockup

This skill is for product-facing visuals, not production frontend implementation.

## Workflow

1. Read minimal project context if the request says "our app", "our dashboard", or "our product".
2. Translate the request into a visual spec with:
   - product category
   - audience
   - surface: desktop, mobile, dashboard, hero section, or campaign creative
   - visual direction
   - negative space needs
3. Prefer clean, intentional layouts over overloaded futuristic dashboards.
4. Use `visual-forge` to generate the asset.

## Prompt additions

- include whether the mockup should feel editorial, SaaS, industrial, consumer, or research-grade
- specify if browser chrome or device framing should be included
- request restrained, credible UI density
- avoid random lorem ipsum walls unless explicitly needed

