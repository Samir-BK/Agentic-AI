# Agentic AI

This repo is where I'm learning **agentic AI** — building small agents with [Agno](https://github.com/agno-agi/agno) to understand how tool use, memory, and multi-agent systems actually work under the hood, rather than just reading about them.

Each file here is a step in that learning process, not a single polished product.

## What I'm learning

- How an LLM agent decides when and how to call a tool
- Giving agents persistent memory across sessions (SQLite-backed)
- Building a multi-agent "team" where agents coordinate on a task
- Wiring an agent up to a real UI (Streamlit)
- Working through breaking changes between framework versions (Agno v2 → v3)

## The agents, in the order I built them

| File | What it explores |
|---|---|
| `agent.py` | First agent — basic Agno `Agent` setup with a model and simple instructions |
| `memory_agent.py` | Persistent user memory — agents that remember facts about a user across runs, backed by SQLite |
| `finance_agent.py` | A tool-using agent applied to finance-related queries |
| `team_agents.py` | Multiple agents working together as a team rather than a single agent |
| `youtube_analyzer.py` + `ui.py` | Putting it together into something usable: a YouTube video summarizer/analyzer with tool use (`YouTubeTools`), memory, and a Streamlit front end |

## Stack

- [Agno](https://github.com/agno-agi/agno) — agent framework
- [Groq](https://groq.com/) — LLM inference
- [Streamlit](https://streamlit.io/) — UI for the YouTube analyzer
- SQLite — agent memory/session storage
- `youtube_transcript_api` — caption retrieval for the YouTube agent

## Running things locally

```bash
git clone https://github.com/Samir-BK/Agentic-AI.git
cd Agentic-AI
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file with:
```
GROQ_API_KEY=your-groq-api-key-here
```

Then run whichever agent you want to poke at:
```bash
python agent.py
python memory_agent.py
python finance_agent.py
python team_agents.py

# or the full app:
streamlit run ui.py
```

## Notes to self

- On **Agno v3** (pre-release) — the `Agent` API changed a fair bit from v2 (e.g. `enable_user_memories` → `update_memory_on_run`). Check the [v3 migration guide](https://docs.agno.com/other/v3-migration) before upgrading.
- `agno.db` / `agno2.db` and their `-shm`/`-wal` sidecars are local memory databases, currently committed but safe to remove/gitignore — they regenerate on first run.

This is a learning repo, so expect rough edges, half-finished experiments, and things that get rewritten as I understand the framework better.