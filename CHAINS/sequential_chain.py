import os
from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1 = PromptTemplate(
    template=' Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template='Generative a 5 pointer summary from the following text \n{text}',
    input_variables=['text']
)

model = init_chat_model(model="groq:llama-3.3-70b-versatile")

parser = StrOutputParser()
chain = prompt1 | model | parser | prompt2 | model | parser

result=chain.invoke({'topic': 'unemployement in india'})
print(result)

chain.get_graph().print_ascii()