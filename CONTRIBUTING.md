# Contributing

## Principles

- Keep the plugin practical. Every skill should help Claude do something concrete.
- Prefer deterministic helper scripts for provider routing and file handling.
- Keep prompts reusable and capability-aware.
- Do not oversell exact text rendering, precise layout, or vector determinism.

## Development loop

1. Edit the plugin under `plugins/visual-forge-studio/`
2. Validate the repo:

```bash
claude plugin validate .
```

3. Test the plugin directly:

```bash
claude --plugin-dir ./plugins/visual-forge-studio
```

4. Test the marketplace flow locally:

```bash
claude plugin marketplace add .
claude plugin install visual-forge-studio@visual-forge
```

## Release notes

- Bump the version in `plugins/visual-forge-studio/.claude-plugin/plugin.json`
- Keep `CHANGELOG.md` current
- Tag releases with:

```bash
claude plugin tag ./plugins/visual-forge-studio
```

