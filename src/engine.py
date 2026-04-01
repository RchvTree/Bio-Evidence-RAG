"""
The core logic of the project, including LLM orchestration (Local/OpenAI) and RAG processes.
"""

import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# 1. Load environment variables from .env file
load_dotenv()

def get_llm():
    """
    Initializes the LLM based on the RUN_MODE in .env.
    """
    run_mode = os.getenv("RUN_MODE", "LOCAL") # Fetches the environment variable; defaults to 'LOCAL' if the key is missing.

    if run_mode == "LOCAL":
        # Connect to local Ollama running Llama 3.2
        return ChatOllama(model = "llama3.2:3b", format="json")
    else:
        # Placeholder for future cloud deployment (e.g., OpenAI)
        pass
