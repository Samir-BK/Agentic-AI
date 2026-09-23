from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv


load_dotenv()

db = SqliteDb(db_file = "agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        db = db,
        markdown=True,
        add_history_to_context = True,
    )

agent = build_agent()

agent.print_response("What is the capital of Nepal?")
agent.print_response("What is the best month to vist it?")