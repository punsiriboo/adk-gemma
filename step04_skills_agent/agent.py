from pathlib import Path

from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.skills import load_skills_from_dir
from google.adk.tools.skill_toolset import SkillToolset

skills = load_skills_from_dir(Path(__file__).parent / "skills")

model = LiteLlm(
    model="lm_studio/google/gemma-4-e4b",
    api_base="http://127.0.0.1:1234/v1",
)

root_agent = Agent(
    model=model,
    name="skills_agent",
    description="A travel helper that uses skills.",
    instruction="Answer user questions. Load a skill when it matches the request.",
    tools=[SkillToolset(skills=skills)],
)
