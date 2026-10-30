from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
    model="lm_studio/google/gemma-4-e4b",
    api_base="http://127.0.0.1:1234/v1",
)

root_agent = Agent(
    model=model,
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge.",
)
