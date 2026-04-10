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

## 🗺️ Project Roadmap

| Phase | Description | Status |
| :--- | :--- | :--- |
| Phase 1: Entity Recognition | Identifying and classifying 'Disease' and 'Drug' entities from text. | Done ✅ |
| Phase 2: Relation Extraction | Understanding. relationships (e.g., treats, causes) between identified entities. | Next 🏃‍♀️ |
| Phase 3: RAG Integration | Augmenting LLM responses with real evidence from PubMed papers (PDF/Text). | TODO 📝 |
| Phase 4: Deployment | Launching a user-friendly web interface using Streamlit. | TODO 📝 |

## 🏆 Milestone Achieved

### Phase 1
I have successfully laid a solid foundation for sustainable software development.

    - Infrastructure
        : Established a professional environment with GitHub integration, virtual environment (venv), secure configuration (.env), and dependency management (requirements.txt)

    - Engine Core
        : Built a robust interface to communicate with a local LLM (Llama 3.2 via Ollama) using LangChain.

    - Orchestration
        : Implemented an efficient LCEL (LangChain Expression Language) pipeline
        : Prompt -> Model -> JSON Parser

    - Data Persistence
        : Developed an automated storage system in utils.py that saves analysis results with precise timestamps for audit trails.

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

**extract_entities()**

    - Description
        : Specifically designed to identify and categorize Diseases and Drugs using a professional Bio-NLP persona.
    
    - Orchestration
        : Leverages LCEL (LangChain Expression Language) for an efficient Prompt | LLM | Parser pipeline.

    - Execution Example
        - Input Text:
            "Patient was prescribed Metformin for Type 2 Diabetes."
        - Output (JSON):
            {
                "diseases": ["Type 2 Diabetes"],
                "drugs": ["Metformin"]
            }

**extract_bio_knowledge()**

    - Description
        : Identifies and extracts complex biological relationships from text in a structured format.

    - Key Featrues
        : Structures findings into Triplets (Subject, Relation, Object) for knowledge graph compatibility.
        : Uses advanced System Instructions to maintain focus and consistency during complex reasoning.
        : Employs Double Brade Escaping {{}} to safely request JSON outputs without syntax errors.

    - Usage
        : The core logic for Phase 2 (Relation Extraction), transforming unstructured bio-text into structured knowledge.

### utils.py
**save_result_to_json()**

    - Description
        : Persists AI-generated results into a permanent JSON file storage.

    - Key Features
        : Implements Timestamp-based versioning (YearMonthDay_Time) for clear audit trails.
        : Uses OS-Agnostic paths via os.path.join to ensure compatibility across Windows, Mac, and Linux.
        : Guarantees Data Integrity with UTF-8 encoding and human-readable (indent=4) formatting.

    - Usage
        : Utility function used in the final step of the engine to save and organize all extracted insights.