# Provider Matrix

## Codex path

Use when:

- the machine already has `codex`
- `codex login status` succeeds
- the user wants the simplest setup

Strengths:

- no API key required
- natural fit for Claude workflows that can call Bash
- strong for iterative image generation and edits

Limits:

- depends on a working local Codex setup
- output control is less explicit than the direct API path

## OpenAI API path

Use when:

- the user wants predictable API-based execution
- the user needs mask-based edits
- the user wants direct control over model, size, quality, or format

Strengths:

- explicit model selection
- easy to parameterize
- supports multipart image-edit flows

Limits:

- requires an API key
- users may need model access or org verification for some image models

