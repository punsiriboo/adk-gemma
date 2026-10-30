import datetime
from zoneinfo import ZoneInfo

from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm


def get_current_datetime(timezone: str = "Asia/Bangkok") -> dict:
    """Return the current date and time for a timezone, e.g. Asia/Bangkok or UTC."""
    now = datetime.datetime.now(ZoneInfo(timezone))
    return {"timezone": timezone, "datetime": now.strftime("%Y-%m-%d %H:%M:%S")}


model = LiteLlm(
    model="lm_studio/google/gemma-4-e4b",
    api_base="http://127.0.0.1:1234/v1",
)

root_agent = Agent(
    model=model,
    name="normal_gemma_agent",
    description="A helpful assistant for user questions.",
    instruction=(
        "Answer user questions to the best of your knowledge. "
        "Call get_current_datetime when asked about the date or time."
    ),
    tools=[get_current_datetime],
)
