import os
from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = init_chat_model(model="groq:llama-3.3-70b-versatile")

parser = StrOutputParser()

# join to make a chain model , prompt and parsers
chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})
print (result)

# to visualise our chain 
chain.get_graph().print_ascii()