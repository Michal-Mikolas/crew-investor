import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

load_dotenv()  # take environment variables from .env

llm=ChatGroq(temperature=0,
	model_name="llama-3.1-70b-versatile",
	api_key=os.getenv("GROQ_API_KEY"),
)

translator = Agent(
	role='Translator',
	goal="To translate given word from English to French.",
	backstory=(
		"You are professional translator. You can translate from English to French and vice versa."
	),
	llm=llm,
	verbose=True,
)

translate = Task(
	description='Translate word "{word}" from English to French.',
	agent=translator,
	expected_output='translated word',
)

crew = Crew(
	agents=[translator],
	tasks=[translate],
	verbose=True,
)

result = crew.kickoff(inputs={'word': 'programming'})  # translate word "programming" to French
print(result)
