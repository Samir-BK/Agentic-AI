from agno.agent import Agent
from agno.models.groq import Groq
from agno.team.mode import TeamMode
from agno.team.team import Team
from dotenv import load_dotenv

load_dotenv()



## Creating Members

english_agent = Agent(
    name="Planner",
    role="Translate in English language",
    model=Groq(id="openai/gpt-oss-120b"),
)
nepali_agent = Agent(
    name="Planner",
    role="Translate in Nepali language",
    model=Groq(id="openai/gpt-oss-120b"),
)
chinese_agent = Agent(
    name="Planner",
    role="Translate in Chinese language",
    model=Groq(id="openai/gpt-oss-120b"),
)


# Create Teams

team = Team(
    name="Query Translation Team",
    mode=TeamMode.tasks,
    model=Groq(id="openai/gpt-oss-120b"),
    members=[english_agent, nepali_agent, chinese_agent],
    instructions=[
        """ All member agents should respond to answer query in their  specific language.
            Don't route to just one agent.
            Output the respone of all agents.
        """,

    ],
    show_members_responses=True,
    markdown=True,
    max_iterations=10,
)

if __name__ == "__main__":
    team.print_response(
        "What is AI?"
    )