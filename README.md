# AI Agents in Action — Companion Code

My working code and notes while reading **[AI Agents in Action](https://www.manning.com/books/ai-agents-in-action)** by Micheal Lanham (Manning).

## Structure

| Folder | Topic |
|--------|-------|
| `ch2/` | Harnessing the power of LLMs — connecting to the OpenAI API |

More chapters will be added as I progress through the book.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install openai python-dotenv
```

Create your local `.env` from the template and add your API key:

```bash
cp .env.example .env
# then edit .env and set OPENAI_API_KEY
```

> `.env` is listed in `.gitignore` and must never be committed.

## Run

```bash
python ch2/connecting.py
```
