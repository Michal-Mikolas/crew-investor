import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

load_dotenv()  # take environment variables from .env

llm=ChatGroq(temperature=0,
	model_name="llama-3.1-70b-versatile",
	api_key=os.getenv("GROQ_API_KEY"),
)

researcher = Agent(
	role='Senior Researcher',
	goal="Uncover groundbreaking technologies",
	backstory="Driven by curiosity, you explore and share the latest innovations.",
	llm=llm,
)

research_task = Task(
	description="Identify the next big trend in the given topic with pros and cons.",
	agent=researcher,
	expected_output='A 3-paragraph report on the given topic. The report will include headline with the exact topic provided as assignment.',
)

crew = Crew(
	agents=[researcher],
	tasks=[research_task],
)

result = crew.kickoff(inputs={'topic': 'AI in healtcare'})
print(result)
