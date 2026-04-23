# Changelog

## 1.0.1 - 2026-04-23

- Fix Windows crash: Codex CLI installs as `.CMD` on Windows, which requires `shell=True` in subprocess calls
- Fix provider routing: skills now instruct Claude to always run the binary instead of preemptively checking for API keys
- Fix temp file leak in Codex path

## 1.0.0 - 2026-04-23

- Initial release
- Added the `gpt-imagen` plugin
- Added Codex-subscription routing through `codex exec`
- Added OpenAI Images API fallback with user-configurable API key and model
- Added skills for frontend mockups, game assets, paper-figure visuals, and image editing
- Added branding assets, example images, install docs, and tutorial docs
