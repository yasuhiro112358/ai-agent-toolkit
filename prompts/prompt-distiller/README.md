# prompt-distiller

Analyze a conversation with an AI and distill a reusable prompt that reproduces the same work in other contexts.

Uses a two-step process: first generate a requirements document, review and refine it, then generate the prompt from it.

[日本語版 / Japanese](README.ja.md)

## How it works

### Step 1: Conversation → Requirements document

1. Copy the full content of `prompts/requirements-extract.md`
2. Paste it at the end of the **same conversation** where the target work was done, then send
3. The AI analyzes the conversation history and outputs a requirements document
4. Review and refine the requirements document as needed

### Step 2: Requirements document → Reusable prompt

**Option A — Continue in the same conversation (recommended):**

1. Copy the full content of `prompts/prompts-generate.md`
2. Paste it at the end of the **same conversation** where Step 1 was done, then send
3. The AI reads the requirements document from the conversation history and outputs a reusable prompt

**Option B — Start a new conversation:**

1. Copy the full content of `prompts/prompts-generate.md`
2. Paste the requirements document from Step 1 into the `## 要件定義書` section at the end
3. Send to a chat AI
4. The AI outputs a reusable prompt based on the requirements document

After either option, save the prompt to a file for reuse.

## Supported tasks

Works for any task type where you repeated a pattern in conversation:

| Category | Examples |
| -------- | -------- |
| Text processing | Summarization, translation, proofreading, writing |
| Code | Review, refactoring, bug fixing, spec interpretation |
| Analysis | Data analysis, comparison, risk assessment |
| Structuring | Organizing information, outline creation, templating |

> Not applicable: merging multiple conversations into one prompt (one conversation → one requirements document is the basic unit).

## Documentation

→ [docs/index.md](docs/index.md)

## File structure

| File | Step | Role |
| --- | --- | --- |
| `prompts/requirements-extract.md` | Step 1 | Prompt that analyzes a conversation and generates a requirements document |
| `prompts/prompts-generate.md` | Step 2 | Prompt that generates a reusable prompt from a requirements document |
| `docs/` | — | Documentation (Diataxis structure) |
