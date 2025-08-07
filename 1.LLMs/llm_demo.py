from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env

llm = OpenAI(model_name = 'gpt-3.5-turbo-instruct') #define model
result = llm.invoke("What is the capital of UK?") #pass through model
print(result)