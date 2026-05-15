# prompt-create-from-conversation

Analyze a conversation with an AI and extract a reusable prompt that reproduces the same work in other contexts.

Uses a two-step process: first generate a requirements document, review and refine it, then generate the prompt from it.

[日本語版 / Japanese](README.ja.md)

## How it works

### Step 1: Conversation → Requirements document

1. Copy the full content of `requirements-create-from-conversation.md`
2. Paste it at the end of the **same conversation** where the target work was done, then send
3. The AI analyzes the conversation history and outputs a requirements document
4. Review and refine the requirements document as needed

### Step 2: Requirements document → Reusable prompt

1. Copy the full content of `prompt-create-from-requirements.md`
2. Paste the requirements document from Step 1 into the `## 要件定義書` section at the end
3. Send to a chat AI
4. The AI outputs a reusable prompt based on the requirements document
5. Save the prompt to a file for reuse

## Documentation

→ [docs/](docs/)

## File structure

| File | Step | Role |
| --- | --- | --- |
| `requirements-create-from-conversation.md` | Step 1 | Prompt that analyzes a conversation and generates a requirements document |
| `prompt-create-from-requirements.md` | Step 2 | Prompt that generates a reusable prompt from a requirements document |
| `requirements.md` | — | Requirements document for this project |
| `docs/` | — | Documentation (Diataxis structure) |
