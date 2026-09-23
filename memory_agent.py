from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv
from rich.pretty import pprint

load_dotenv()

db = SqliteDb(db_file = "agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        db = db,
        markdown=True,
        add_history_to_context = True,
        update_memory_on_run=True
    )

agent = build_agent()

user_id = "samir@gmail.com"
agent.print_response("My name is Samir, and I am a software engineer and AI engineer and I live in helsinki.", user_id = user_id)
agent.print_response("Who I am?", user_id = user_id)

memorires = agent.get_user_memories(user_id = user_id)
print("Memories: \n", memorires)