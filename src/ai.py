from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
#Here with the help of load_doteenv HF_TOKEN  is assigned to the model

def load_model(repo_id):
    llm = HuggingFaceEndpoint(
    repo_id=repo_id,  # Chat-capable model
    task="text-generation"
    )

    chat_model = ChatHuggingFace(llm=llm)
    return chat_model
