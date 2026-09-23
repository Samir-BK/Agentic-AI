from agno.agent import Agent
from agno.models.groq import Groq
from ddgs import DDGS
from dotenv import load_dotenv

load_dotenv()


def web_search(query: str) -> list[dict[str, str]]:
    """Return search results without letting an empty search crash the agent."""
    try:
        return list(DDGS().text(query, max_results=5))
    except Exception as error:
        return [{"error": f"Search failed: {error}"}]


def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        markdown=True,
        instructions=[
            "You are an expert research assistant.",
            "Use only the research results included in the user message.",
            "If the results are empty or contain an error, say that the information could not be verified.",
            "Do not invent investment amounts or startup names.",
            "Cite the sources used in your answer.",
        ],
        add_datetime_to_context=True,
    )

groq_agent = build_agent()

query = "highest funded startup Y Combinator Spring 2026 Demo Day investment"
research_results = web_search(query)
groq_agent.print_response(
    f"Which startup received the highest investment at Y Combinator Demo Day Spring 2026?\n\n"
    f"Research results for {query!r}:\n{research_results}"
)