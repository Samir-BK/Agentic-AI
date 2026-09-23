from agno.agent import Agent # Agent
from agno.models.groq import Groq # Model

from dotenv import load_dotenv
load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        markdown = True,
        instructions = "You are a helpful and expert travel agent."
    )

groq_agent = build_agent()

groq_agent.print_response("What is your knowöedge cutoff?")