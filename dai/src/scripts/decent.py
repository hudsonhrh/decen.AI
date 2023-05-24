from langchain.llms import OpenAI
import os

# Use os.environ to get environment variables
openai_api_key = os.environ.get('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("Missing environment variable: 'NEXT_PUBLIC_OPENAI'")


llm = OpenAI(openai_api_key=openai_api_key, temperature=.9)


from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)



print(llm(prompt.format(product="DAO AI tools")))