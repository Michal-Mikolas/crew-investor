import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

load_dotenv()  # take environment variables from .env

llm=ChatGroq(temperature=0,
	model_name="llama-3.1-70b-versatile",
	api_key=os.getenv("GROQ_API_KEY"),
)

adviser = Agent(
	role='Stocks Adviser',
	goal="Advise specific stocks ticker symbols based on client's request. The ticker symbols will then be passed to other experts and used for advanced trading analysis.",
	backstory=(
		"You are expert at financial markets, stocks, ETFs etc. You have deep knowledge about all the specific companies, financial markets, commodities and so on."
	),
	llm=llm,
	verbose=True,
)

advise_tickers = Task(
	description="Advise specific ticker symbols based on user's request. The ticker symbols will then be passed to other experts and used for advanced trading analysis.",
	agent=adviser,
	expected_output='Ticker symbols separated by comma. Nothing else, just the symbols.',
)

crew = Crew(
	agents=[adviser],
	tasks=[advise_tickers],
	verbose=True,
)

result = crew.kickoff(inputs={'query': 'Provide 5 ticker symbols of companies from the Semiconductor industry.'})
print(result)
