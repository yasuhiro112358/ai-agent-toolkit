# ai-agent-toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A collection of reusable prompts, skills, and agents for AI-powered workflows.

[日本語版 / Japanese](README.ja.md)

---

## What is this?

This repository contains prompts and skills you can use with any AI agent or generative AI service — Claude Code, Claude.ai, ChatGPT, and more.

- **Claude Code users**: Copy a skill folder to `~/.claude/skills/` and invoke it with `/skill-name`
- **Any chat AI users**: Copy the prompt content and paste it directly into a conversation

---

## Prompts

Standalone prompts — no Claude Code required. Paste the file contents into any chat AI.

| Name | Description | Dependencies |
| --- | --- | --- |
| [diagram-keeper](prompts/diagram-keeper/README.md) | Generate and maintain Mermaid class diagrams and call graphs via generative AI, keeping them in sync as code evolves | Python 3.8+, VS Code + Mermaid Chart extension |
| [prompt-create-from-conversation](prompts/prompt-create-from-conversation/README.md) | Generate a reusable prompt from a completed AI conversation | None |
| [task-management](prompts/task-management/README.md) | Prompt-driven task management system that runs inside any chat AI — no API key, server, or custom app required | None |

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

## License

MIT License — see [LICENSE](LICENSE) for details.
