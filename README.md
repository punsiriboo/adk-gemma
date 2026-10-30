# adk-gemma

ADK agents talking to **Gemma on LM Studio** (OpenAI-compatible local API).

Two agent folders:

| Folder | Type | Role |
|--------|------|------|
| `normal_agent/` | `Agent` (LlmAgent) | Chat + `get_current_datetime` tool |
| `workflow_agent/` | `SequentialAgent` | Planner → responder pipeline |

Switch with `AGENT_KIND=normal` or `AGENT_KIND=workflow` in `.env`.

## Project Structure

```
adk-gemma/
├── normal_agent/      # Single chat agent
├── workflow_agent/    # Sequential planner → responder
├── shared/            # LiteLLM/LM Studio model + tools
├── app/               # ADK entry (loads AGENT_KIND)
├── tests/
├── AGENTS.md
└── pyproject.toml
```

## Requirements

- **uv** — [Install](https://docs.astral.sh/uv/getting-started/installation/)
- **agents-cli** — `uv tool install google-agents-cli`
- **LM Studio** — load a Gemma model and start the local server (default `http://127.0.0.1:1234/v1`)

## Quick Start

1. In LM Studio: load Gemma, start the server, note the model id (set `LMSTUDIO_MODEL` in `.env` if different from `gemma-3-4b-it`).

2. Install packages:

```bash
agents-cli install
```

3. Pick an agent in `.env` (`AGENT_KIND=normal` or `workflow`), then:

```bash
agents-cli playground
# or
agents-cli run "ตอนนี้กี่โมงแล้ว"
```

## Commands

| Command              | Description                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------- |
| `agents-cli install` | Install dependencies using uv                                                         |
| `agents-cli playground` | Launch local development environment                                                  |
| `agents-cli lint`    | Run code quality checks                                                               |
| `agents-cli eval`    | Evaluate agent behavior (generate, grade, analyze, and more — see `agents-cli eval --help`) |
| `uv run pytest tests/unit tests/integration` | Run unit and integration tests                                                        || [A2A Inspector](https://github.com/a2aproject/a2a-inspector) | Launch A2A Protocol Inspector                                                        |

## 🛠️ Project Management

| Command | What It Does |
|---------|--------------|
| `agents-cli scaffold enhance` | Add CI/CD pipelines and Terraform infrastructure |
| `agents-cli infra cicd` | One-command setup of entire CI/CD pipeline + infrastructure |
| `agents-cli scaffold upgrade` | Auto-upgrade to latest version while preserving customizations |

---

## Development

Edit your agent logic in `app/agent.py` and test with `agents-cli playground` - it auto-reloads on save.

## Deployment

```bash
gcloud config set project <your-project-id>
agents-cli deploy
```

To add CI/CD and Terraform, run `agents-cli scaffold enhance`.
To set up your production infrastructure, run `agents-cli infra cicd`.

## Observability

Built-in telemetry exports to Cloud Trace, BigQuery, and Cloud Logging.

## A2A Inspector

This agent supports the [A2A Protocol](https://a2a-protocol.org/). Use the [A2A Inspector](https://github.com/a2aproject/a2a-inspector) to test interoperability.
See the [A2A Inspector docs](https://github.com/a2aproject/a2a-inspector) for details.
