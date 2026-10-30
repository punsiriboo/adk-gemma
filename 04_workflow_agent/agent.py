from google.adk.agents import Agent, SequentialAgent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
    model="lm_studio/google/gemma-4-e4b",
    api_base="http://127.0.0.1:1234/v1",
)

planner = Agent(
    model=model,
    name="planner",
    description="Writes a short plan for answering the user.",
    instruction="Write a short numbered plan (3-5 steps) to answer the user. Do not answer yet.",
    output_key="plan",
)

responder = Agent(
    model=model,
    name="responder",
    description="Writes the final answer using the plan.",
    instruction="Use this plan:\n{plan}\n\nWrite the final answer for the user.",
)

root_agent = SequentialAgent(
    name="workflow_gemma_agent",
    description="Planner then responder.",
    sub_agents=[planner, responder],
)
