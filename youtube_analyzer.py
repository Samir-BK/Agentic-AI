from textwrap import dedent

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint
from dotenv import load_dotenv

load_dotenv()

db = SqliteDb(db_file = "agno2.db")
db.clear_memories()
def build_yt_agent():
    return Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    tools = [YouTubeTools()],
    db = db,
    markdown=True,
    add_history_to_context = True,
    update_memory_on_run=True,
    instructions = [
        "You are a YouTube video analyzer and summarizer.",
        "When given a YouTube URL, first call get_youtube_video_data to get the title, channel, and description.",
        "Then call get_youtube_video_captions to retrieve the full transcript.",
        "If the user asks for key moments, chapters, ors timestamps, also call get_youtube_video_timestamps.",
        "Base your summary strictly on the retrieved captions and metadata — never invent content the video didn't cover.",
        "If captions are unavailable or empty, tell the user clearly instead of guessing at the content.",
        "Structure summaries as: a 1-2 sentence overview, then key points as bullets, then (if timestamps were requested) a timestamped outline.",
        "Keep summaries proportional to video length — a 5-minute video doesn't need a 20-bullet breakdown.",
        "If the user asks a specific question about the video instead of a general summary, answer using the transcript content directly rather than producing a full summary.",
        "Always mention the video title and channel name at the start of your response.",
    ]
)  



# youtube_agent.print_response("Summarize this video: https://www.youtube.com/watch?v=sBqrw-Ehhc0", stream = True)