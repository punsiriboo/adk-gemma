# adk-gemma

Codelab: build ADK agents on **Gemma 4 running locally in LM Studio** (OpenAI-compatible API on `http://127.0.0.1:1234/v1`).

Slides: open [`index.html`](index.html) in a browser (DevFest Chengdu, EN + 简体中文).

## Steps

| Folder | What it shows |
|--------|---------------|
| `step01_basic_agent/` | `Agent` + LiteLlm → LM Studio, with a `get_current_datetime` function tool |
| `step02_mcp_agent/` | `McpToolset` connected to the Airbnb MCP server (`npx`) |
| `step03_skills_agent/` | `SkillToolset` loading `skills/trip-itinerary` and `skills/packing-list` |
| `step04_workflow_agent/` | ADK 2.x `Workflow`: planner → responder via `output_key` |

Every agent uses the same model:

```python
LiteLlm(
    model="lm_studio/google/gemma-4-e4b",
    api_base="http://127.0.0.1:1234/v1",
)
```

## Requirements

- **LM Studio** with `google/gemma-4-e4b` downloaded
- **Python** 3.11+
- **Node.js** 18+ (only for `step02_mcp_agent`)

## Quick Start

1. Start Gemma in LM Studio:

```bash
lms get google/gemma-4-e4b
lms load google/gemma-4-e4b
lms server start
curl http://localhost:1234/v1/models   # the "id" must match the model string above
```

2. Install ADK and LiteLLM:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install "google-adk>=2.2" "litellm>=1.84"
```

3. Run the dev UI from the repo root and pick a `stepXX_*` agent in the top-left menu:

```bash
adk web          # http://127.0.0.1:8000
# or chat in the terminal
adk run step01_basic_agent
```

## Try these prompts

| Agent | 中文 | English |
|-------|------|---------|
| `step01_basic_agent` | 成都现在几点？ | What time is it in Chengdu now? |
| `step02_mcp_agent` | 帮我找成都 11 月 15 日入住两晚的民宿，2 位成人 | Find me a place to stay in Chengdu for 2 nights from Nov 15, 2 adults |
| `step03_skills_agent` | 帮我规划成都 3 天行程 | Plan a 3-day trip to Chengdu |
| `step04_workflow_agent` | 帮我安排一个成都周末两日游 | Plan a 2-day weekend trip in Chengdu for me |

## Troubleshooting

- **404 / model not found** — the model id doesn't match `GET /v1/models`; copy the exact id.
- **Connection refused** — LM Studio server isn't running; `lms server start`.
- **No tool calls** — use a tool-capable model and say in the instruction when to call the tool.
