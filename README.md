# Bio-Evidence RAG
## A specialized RAG (Retrieval-Augmented Generation) system designed for biological evidence analysis.

## 💰 Cost Optimization & Deployment Strategy
    This project is designed to provide high-performance reasoning while maintaining zero development costs and ensuring user privacy.

### 1. Hybrid Environment Design

| Mode | Environment | Model Used | Cost |
| :--- | :--- | :--- | :--- |
| Local | Development | Llama 3.2 3B | $0 (Free) |
| BYOK | Deployment | User's API Key | User-Funded |

### 2. Strategic Model Selection

    - Llama 3.2 3B (Selected)
        : Chosen for its optimal balance between local hardware efficiency and complex reasoning depth.
    - Cost Efficiency
        : Running locally during the development phase allows for unlimited testing with zero API overhead.
    - Scalability & Privacy (BYOK)
        : For deployment, the Bring Your Own Key model ensures that the system is sustainable for the maintainer and secure for the user.

## ⚙️ Configuration Setup
    To run this project, you must set up your environment variables.

### Step 1: Create Envrionment File
Copy the provided .env.example to a new file named .env:

    cp .env.example .env

### Step 2: Configure Variables
Edit your .env file based on your current phase.
(Refer to .env.example for the required format.)

## 🛠️ Libraries & Rationale
    Key Decision: I prioritized Industry-Standard Libraries to focus on scalable system design and probelm-solving rather than low-level implementation.

| Library | Role | Selection Rationale (vs. Alternative) |
| :--- | :--- | :--- |
| LangChain | AI Orchestration | Chosen for its vast ecosystem and modularity over LlamaIndex (too data-specific) |
| Ollama | Local Runtime | Selected for its CLI-centric workflow and ease of integration vs. LM Studio (GUI-only) |
| python-dotenv | Security | The industry standard for secure credential management over manual os parsing |


## 🚀 Core Functions
### engine.py
**get_llm()**

    - Description
        : Initializes and returns the ChatOllama language model instance.
    
    - Key Features
        : Automatically loads environment variables from a .env file using dotenv.
        : Configures the model parameters (e.g., model name, temperature) for consistent responses.
    
    - Usage
        : Used throughout the engine to process prompts and generate AI responses.