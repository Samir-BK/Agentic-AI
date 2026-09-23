from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()


def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        tools=[
            YFinanceTools(
                enable_stock_price=True,
                enable_historical_prices=True,
                enable_company_info=True,
                enable_analyst_recommendations=True,
                enable_company_news=True,
            )
        ],
        markdown=True,
        description="You are a comprehensive investment analyst with access to all financial data functions.",
        instructions=[
            "Use the financial tools for current market data.",
            "Format your response using markdown and use tables to display data.",
            "Provide detailed analysis and insights based on the data.",
            "Include relevant financial metrics and recommendations.",
            "State clearly when data is unavailable; do not invent values.",
        ],
        add_datetime_to_context=True,
    )

groq_agent = build_agent()

groq_agent.print_response(
    "Share the current NVDA stock price and its recent historical performance. "
    "Include the retrieved data sources and explain the time period used."
)