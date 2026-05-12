# diagram-keeper

Generate and maintain Mermaid class diagrams and call graphs for your codebase using generative AI, keeping them in sync as code evolves.
Works with any chat AI (Claude.ai, ChatGPT, etc.) — no API key or external service required.

[日本語版 / Japanese](README.ja.md)

## Two roles

### User (read and use diagrams)

Preview existing class diagrams and call graphs in VS Code, and derive sequence diagrams for any scenario on demand. No `bundle.py` needed.

### Admin (create and maintain diagrams)

Bundle source code with `bundle.py` and paste it along with a prompt into a chat AI to update the master diagrams. Supports 9 languages: C/C++, Java, C#, Python, TypeScript, JavaScript, PHP, Rust, Visual Basic.

## Requirements

### User

- VS Code + [Mermaid Chart extension](https://marketplace.visualstudio.com/items?itemName=MermaidChart.vscode-mermaid-chart)
- Generative AI (Claude.ai, ChatGPT, etc.)

### Admin (in addition to the above)

- Python 3.8+ (standard library only)

## Documentation

→ [docs/index.md](docs/index.md)

## File structure

| Path | Role |
| --- | --- |
| `scripts/bundle.py` | Convert source tree to MANIFEST format |
| `prompts/diagrams-upsert.md` | Upsert master diagrams (Create + Update) |
| `prompts/diagrams-delete.md` | Delete entries from master diagrams |
| `prompts/diagrams-convert-to-sequence.md` | Derive sequence diagrams from master diagrams |
| `docs/` | Documentation (Diataxis structure) |
