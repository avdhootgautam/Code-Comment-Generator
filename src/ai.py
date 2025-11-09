from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from crewai import LLM
import os
load_dotenv()
#Here with the help of load_doteenv HF_TOKEN  is assigned to the model

# def load_model(repo_id):
#     print(f"In a load_model function")
#     llm = HuggingFaceEndpoint(
#     repo_id=repo_id,  # Chat-capable model
#     task="text-generation"
#     )

#     chat_model = ChatHuggingFace(llm=llm)
#     print(f"In a load_model function,chat_model created")
#     return chat_model

def load_model(repo_id):
    print("In a load_model function")

    llm=LLM(
        model=f"huggingface/{repo_id}",
        temperature=0,
        base_url="https://router.huggingface.co/hf-inference",
        api_key=os.getenv("HF_TOKEN")
    )

    print("Model loaded using CrewAI LLM")
    return llm