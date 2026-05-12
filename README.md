# claude-code-skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/yasuhiro112358/claude-code-skills/pulls)

A collection of reusable Claude Code skills and prompts.

[日本語版 / Japanese](README.ja.md)

---

## What is this?

This repository contains [Claude Code](https://claude.ai/code) skills (`SKILL.md` format) and standalone prompts that you can use in your own projects.

- **Claude Code users**: Copy a skill folder to `~/.claude/skills/` and invoke it with `/skill-name`
- **Claude.ai / API users**: Copy the prompt content and paste it directly into a conversation

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yasuhiro112358/claude-code-skills.git

# Copy a skill to your Claude Code skills directory
cp -r claude-code-skills/skills/smart-commit ~/.claude/skills/

# Now use it in Claude Code
# /smart-commit
```

---

## Skills

| Name | Category | Description | Dependencies |
| --- | --- | --- | --- |
| *(coming soon)* | - | - | - |

---

## Agents

| Name | Description | Tools Required |
| --- | --- | --- |
| *(coming soon)* | - | - |

---

## Prompts

Standalone prompts — no Claude Code required. Paste the file contents into any chat AI.

| Name | Description | Dependencies |
| --- | --- | --- |
| [generate-prompt-from-conversation](prompts/generate-prompt-from-conversation.md) | Generate a reusable prompt from a completed AI conversation | None |
| [diagram-keeper](prompts/diagram-keeper/) | Generate and maintain Mermaid class diagrams and call graphs via generative AI, keeping them in sync as code evolves | Python 3.8+, VS Code + Mermaid Chart extension |
| [task-management](prompts/task-management/) | Prompt-driven task management system that runs inside any chat AI — no API key, server, or custom app required | None |

---

## Contributing

Contributions are welcome! Please open an issue or pull request.

When contributing a skill, ensure:

- No personal information or private file paths
- No dependencies on private repositories
- Self-contained and usable in any project

---

## License

MIT License — see [LICENSE](LICENSE) for details.
