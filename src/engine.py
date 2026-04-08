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
    Initializes the LLM based on the RUN_MODE in .env
    """
    run_mode = os.getenv("RUN_MODE", "LOCAL") # Fetches the environment variable; defaults to 'LOCAL' if the key is missing.

    if run_mode == "LOCAL":
        # Connect to local Ollama running Llama 3.2
        return ChatOllama(model = "llama3.2:3b", format="json")
    else:
        # Placeholder for future cloud deployment (e.g., OpenAI)
        pass

def extract_entities(text):
    """
    Extracts 'Disease' and 'Drug' entities from the given text using LLM
    """
    llm = get_llm()

    # Define the System Prompt (Instructions for the API)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", (
            "You are a professional Bio-NLP assistant. "
            "Extract entities from the text and return them in JSON format with keys: 'diseases' and 'drugs'."
        )),
        ("user", "Text to analyze: {input_text}")
    ])

    # Createt a Chain (The Orchestration)
    # LCEL (LangChain Expression Language) syntax: prompt | model
    chain = prompt_template | llm | JsonOutputParser()

    # Invoke the chain and get the response
    response = chain.invoke({"input_text": text})
    return response

# --- Test Execution ---
if __name__ == "__main__":
    sample_text = "Patient was prescribed Metformin for Type 2 Diabetes."

    print("--- Extracting Bio-Entities ---")
    result = extract_entities(sample_text)

    # Print the structured result (JSON)
    print(result)