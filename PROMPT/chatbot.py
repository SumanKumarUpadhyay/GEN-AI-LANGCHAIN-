import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()
# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mistral-7B-Instruct-v0.2",
#     temperature=0.7,
#     max_new_tokens=256,
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )

# model = ChatHuggingFace(llm=llm)

# model = ChatGroq(model="llama-3.3-70b-versatile")

model = init_chat_model(model="groq:llama-3.3-70b-versatile")

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('you:  ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exist':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)