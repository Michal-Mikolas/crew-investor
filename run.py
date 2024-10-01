import os
from dotenv import load_dotenv
from crewai import LLM, Agent, Task, Crew

load_dotenv()  # take environment variables from .env

llm = LLM(model="groq/llama-3.2-3b-preview", temperature=0.0)

adviser = Agent(
	role='Stocks Adviser',
	goal="Advise specific stocks ticker symbols based on client's request. The ticker symbols will then be passed to other experts and used for advanced trading analysis.",
	backstory="You are expert at financial markets, stocks, ETFs etc. You have deep knowledge about all the specific companies, financial markets, commodities and so on.",
	llm=llm,
	verbose=True,
)

advise_tickers = Task(
	description="Advise specific ticker symbols based on user's request. The ticker symbols will then be passed to other experts and used for advanced trading analysis. User request: {request}.",
	agent=adviser,
	expected_output='Ticker symbols separated by comma. Nothing else, just the symbols.',
)

crew = Crew(
	agents=[adviser],
	tasks=[advise_tickers],
	verbose=True,
)

result = crew.kickoff(inputs={'request': '5 companies from the Semiconductor industry'})
print(result)
