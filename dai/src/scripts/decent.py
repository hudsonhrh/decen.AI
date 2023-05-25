from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
import os

# Use os.environ to get environment variables
openai_api_key = os.environ.get('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("Missing environment variable: 'NEXT_PUBLIC_OPENAI'")



llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.0)
math_llm = OpenAI(openai_api_key=openai_api_key,temperature=0.0)
tools = load_tools(
    ["human", "llm-math"], 
    llm=math_llm,
)

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent_chain.run("What's my friend Eric's surname?")