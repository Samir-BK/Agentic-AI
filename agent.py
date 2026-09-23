from agno.agent import Agent # Agent
from agno.models.groq import Groq # Model

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        markdown = True,
        instructions = "You are a helpful and expert travel agent"
    )