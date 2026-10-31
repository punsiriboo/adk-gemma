from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.load_memory_tool import load_memory_tool


async def save_to_memory(callback_context):
    """After each turn, save this conversation so other sessions can recall it."""
    await callback_context.add_session_to_memory()


model = LiteLlm(
    model="lm_studio/google/gemma-4-e4b",
    api_base="http://127.0.0.1:1234/v1",
)

root_agent = Agent(
    model=model,
    name="memory_agent",
    description="An assistant that remembers past conversations.",
    instruction=(
        "Answer user questions. "
        "If the user asks about something from a past conversation, "
        "call load_memory with a short keyword query first."
    ),
    tools=[load_memory_tool],
    after_agent_callback=save_to_memory,
)
