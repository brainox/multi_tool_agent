from google.adk.agents import LlmAgent
from google.adk.tools import google_search

MODEL="gemini-2.0-flash-001"

idea_agent = LlmAgent(
    model=MODEL,
    name="IdeaAgent",
    description="Brainstorms creative and exciting weekend travel ideas based on user preferences or requests.",
    instruction="You are a creative travel agent. Use the tool to brainstorm and respond to the user with 3 exciting weekend trip ideas based on the user's request.",
    disallow_transfer_to_peers=True,
)

refiner_agent = LlmAgent(
    model=MODEL,
    name="RefinerAgent",
    description="Reviews provided travel ideas and selects only those estimated to cost under the provided budget for a weekend trip.",
    instruction="Use your tools to review the provided trip ideas. Respond ONLY with the ideas likely under the provided budget for a weekend. If none seem to fit, say so.",
    tools=[google_search],
    disallow_transfer_to_peers=True,
)

root_agent = LlmAgent(
    model=MODEL,
    description=(
        "Agent to plan a trip."
    ),
    instruction=f"""You are a Trip Planner, coordinating specialist agents.
    Your goal is to provide budget-friendly weekend trip ideas. For each user request, follow the below instructions:
        1. First, use "{idea_agent}" to brainstorm ideas based on the user's request.
        2. Then, use "{refiner_agent}" to take those ideas to filter them for the provided budget.
        3. Present the final, refined list to the user along with the budget.
    """,
    sub_agents=[idea_agent, refiner_agent],
)