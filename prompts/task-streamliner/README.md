# task-streamliner

Prompt-driven task management system that runs inside any chat AI.
Paste a single file into Claude.ai, ChatGPT, or any chat UI — no API key, server, or custom app required.

[日本語版 / Japanese](README.ja.md)

## How it works

1. Open `templates/tasks.md` in a text editor
2. Copy the entire file and paste it into a chat UI (Claude.ai, ChatGPT, etc.)
3. Send — the AI automatically processes Inbox items and runs CPM scheduling
4. Give instructions in natural language
5. Type "output" to receive the full file, then overwrite `templates/tasks.md`

## Requirements

- Any conversational chat AI (Claude.ai, ChatGPT, etc.) — account only
- A text editor

## Documentation

→ [docs/index.md](docs/index.md)

## File structure

| Path | Role |
| --- | --- |
| `templates/tasks.md` | Task data + AI behavior definition (single source of truth) |
| `prompts/tasks-operate.md` | Standalone behavior definition (recovery use only) |
| `docs/` | Documentation (Diataxis structure) |
