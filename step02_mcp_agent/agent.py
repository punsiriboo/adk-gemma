from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool import McpToolset, StdioConnectionParams
from mcp import StdioServerParameters

airbnb_tools = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
        ),
        timeout=30,
    ),
)

model = LiteLlm(
    model="lm_studio/google/gemma-4-e4b",
    api_base="http://127.0.0.1:1234/v1",
)

root_agent = Agent(
    model=model,
    name="travel_assistant",
    description="A helpful travel assistant.",
    instruction="Answer user questions. Use the Airbnb tools to find places to stay.",
    tools=[airbnb_tools],
)
