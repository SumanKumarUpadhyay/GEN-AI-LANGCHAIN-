import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# Load .env file
load_dotenv()

# ✅ Set your Hugging Face token (from .env or directly)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("new_api") or "hf_your_token_here"

# ------------------------------
# Initialize both models
# ------------------------------

# 1️⃣ Groq Model
model1 = ChatGroq(model="llama-3.3-70b-versatile")

# 2️⃣ Hugging Face Model (via endpoint)
# Using a lightweight free model (no payment required)
hf_endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # ✅ free model
    task="text-generation",
    temperature=0.7,
    max_new_tokens=256
)

model2 = ChatHuggingFace(llm=hf_endpoint)

# ------------------------------
# Define prompts
# ------------------------------

prompt1 = PromptTemplate.from_template("Summarize this text:\n{text}")
prompt2 = PromptTemplate.from_template("Explain this text simply:\n{text}")

parser = StrOutputParser()

# ------------------------------
# Parallel chain setup
# ------------------------------

chain = RunnableParallel(
    notes=prompt1 | model1 | parser,
    explanation=prompt2 | model2 | parser
)

# ------------------------------
# Run example
# ------------------------------

text = "Artificial Intelligence helps automate complex tasks and enhance human productivity."

result = chain.invoke({"text": text})

# ------------------------------
# Display results
# ------------------------------

print("\n🧠 Notes from Groq Model:\n", result["notes"])
print("\n💬 Explanation from Hugging Face Model:\n", result["explanation"])
