# Personal Study Log
## Goal: To master core programming concepts and document the learning process systematically on GitHub.


### 💰 Strategy for Cost Optimization: Local LLM & BYOK

1. **The Challenge: API Costs vs. Development Needs**

    : Integrating AI requires API calls, which incur costs. During the Development Phase, frequent testing can lead to high expenses. Therefore, I needed a solution that provides "High Reliability" and "Accuracy" while being "Free to use."

2. **Solution: Local LLM for Development**

    : I decided to run AI models locally to eliminate API fees during testing.

        - Options considered & Evaluation:
            - Gemma 2 2B
                : High speed, but lacked sufficient reasoning depth for complex tasks.
            - Phi-3.5 Mini
                : Excellent logic, but had relatively limited community doecumentation compared to Llama.
            - Llama 3.2 3B (Selected)
                : It offers the best balance between performance and resource consumption. It runs smoothly on my local hardware while maintaining a higher level of reasoning capability compared to smaller 2B models.

3. **Deployment Strategy: BYOK (Bring Your Own Key)**

    : For the Deployment Phase, I adopted the BYOK method.

        - Target Audience
            : Since the project is intended for developers on GitHub, requiring them to use their own API keys is a reasonable approach.

        - Future Scalability
            : If this evolves into a public service, I can implement "Token Usage Limits" or switch to a "Paid Subscription Model" to generate revenue and offset costs.

        - Security & Privacy
            : The BYOK approach ensures that user data remains within their own accounts, addressing potential Security and Privacy concerns effectively.

### 📦 Packages and __init__.py

**1. Concepts: Modules vs. Packages**

    - Modules
        : A single python file (.py) containing code.

    - Packages
        : A directory (folder) that collects multiple modules to organize them logically.

**2. The Role of __init__.py**

    - Package Declaration
        : It tells Python that the directory should be treated as a package. This allows you to import modules from that folder using dot notation (e.g., import folder.module).

    - Implicit Significance
        : Even if the file is empty, its presence marks the folder as a functional unit in the Python ecosystem. It acts like a "flag" for the interpreter.

    - Initialization
        : It can be used to execute initialization code for a package or to limit which modules are exposed to the outside world.

**3. Why Use It?**

    - Organization
        : Keeps related code together and maintains a clean project structure.
    
    - Accessibility
        : Simplifies the process of importing various functions and classes across different files.

### 🔠 Natural Language Processing: NER (Named Entity Recognition)

**1. Definition**

    : NER is a subtask of information Extraction that seeks to locate and classify named entities mentioned in unstructured text into predefined categories.

**2. Common Categories**

    - PER (Person)
        : Real or fictional characters

    - ORG (Organization)
        : Companies, agencies, or institutions
    
    - LOC (Location)
        : Geographical areas and political entities

    - DATE/TIME
        : Specific dates or time periods

**3. Why It Matters**

    : NER allows machines to understand the context and entities within a sentence, transforming raw text into structured data.
    : It is fundamental step in building Intelligent Search, Chatbots, and Recommendation Systems.

### 🛠️ Essential Libraries & Selection Rationale
This section outlines the core libraries used in this project and technical reasoning behind their selection over existing alternatives.

**1. LangChain -> Framework**

    - Role
        : A framework for developing applications powered by LLMs. It "chains" different components like memory, document loaders, and model providers.

    - Alternatives
        - LlamaIndex
            : Highly specialized in data retrieval (RAG). However, it is less flexible than LangChain when building complex logic or agents.
        - Haystack
            : Robust for enterprise-level search but has a smaller community and fewer learning resources compared to LangChain.
    
    - Why this tool?
        : It is the "De Facto" standard in the AI industry. Its modularity and massive ecosystem a llow for rapid prototyping and seamless scaling. Unlike specific tools, LangChain acts as a "Swiss Army Knife" for LLM orchestration. 

**2. Ollama -> Local Runtime**

    - Role
        : A lightweight runtime that allows running open-source LLMs (like Llama 3.2) locally.

    - Alternatives
        - LM Studio
            : Provides a great GUI for beginners but is difficult to integrate into a Python-based automated workflow or CLI environment.
        - LocalAI/vLLM
            : High-performance options but require complex setup and significant system resources.

    - Why this tool?
        : It strikes the best balance between simplicity and power. Its CLI-first approach and local API endpoint make it perfect for developer-centric prototyping.

**3. python-dotenv -> Environment Management**

    - Role
        : A library to manage environment variables from a .env file.
    
    - Alternatives
        - Native os module
            : Requires manual parsing of files, leading to more boilerplate code.
        - Pydantic Settings
            : Very powerful for large-scale apps but overkill for a learning project.

    - Why this tool?
        : It is the industry standard for simplicity. It ensures security with minimal code, allowing me to focus on the core AI logic without worrying about credential leaks.

**4. langchain_core -> Standard Interface**

Defining the "Rulebook" for messages, LCEL, and parsers.

    - ChatPromptTemplate
        : A tool for Prompt Engineering that structures instructions for the AI.

        - Prompting Strategy: Raw Strings vs. ChatPromptTemplate
            : While LLMs can understand simple Python strings, using ChatPromptTemplate is the professional standard for the following reasons:

                - Role Management
                : Clearly distinguishes between System, Human, and AI roles for better persona maintenance.
            
                - Variable Injection
                : Safely and cleanly injects dynamic inputs (e.g., {topics}) into prompts.

                - LCEL Compatibility
                : Designed to work seamlessly with the LangChain Expression Language (| pipe syntax) for modularity.

    - JsonOutputParser
        : Converts natural lnaguage AI responses into machine-readable JSON format.

### 💾 Data Persistence
Why Save Engine Results to Text Files?

    - Data Persistence
        : AI responses are volatile. Saving them ensures the extracted insights are permanently stored and retrievable.

    - Next Step Preparation
        : The output of Phase 1 (Entities) serves as the input for Phase 2 (Relations). File storage acts as a bridge between project phases.

    - Batch Processing
        : Essential for handling large volumes of text systematically without overwhelming the system's memory.


## 🚀 Project Progress
### 🧠 engine.py
**get_llm()**
1. Code Structure

The get_llm() function serves as the Entry Point for our AI model. It ensures that the model is always initialized with the correct security settings.

2. Technical Decisions

- Environment Loading

    : By calling load_dotenv() inside the function, we guarantee that the API keys and configurations are avaliable before the model starts.

- Error Prevention

    : Centralizing the LLM creation prevents redundant code and makes it easier to swap models (e.g., switching from Llama 3.2 to another model) in one place.

3. What I Learned

- How to bridge the gap between local system files (.env) and Python code using the os module.

- The importance of Encapsulation

    : Wrapping model creation in a function keeps the rest of the code clean.

**extract_entities()**
1. Code Structure

The extract_entities() function is the core logic for processing unstructured bio-medical text. It transforms raw input into structured JSON data containing specific entities like 'Diseases' and 'Drugs' by orchestrating a LangChain pipeline.

2. Technical Decisions

- System Prompting (Expert Persona)

    : By assigning the role of a "Professional Bio-NLP assistant", we ensure the LLM understands the specialized medical context and adheres strictly to the required JSON output format.

- LCEL (LangChain Expression Language) Orchestration

    : Usint the | (pipe) operator simplifies the complex workflow (Prompt -> LLM -> Parser) into a single, readable, and maintainable pipeline.

- Native Output Parsing (JsonOutputParser)

    : Instead of manually parsing text with regular expressions (Regex), we use a dedicated parser to convert the AI's natural language response directly into a Python dictionary.

3. What I Learned

- The Power of LCEL

    : I learned how declarative syntax makes AI orchestration much simpler compared to writing manual API calls and handling intermediate data flow.

- Bridging AI and Software Data

    : I understood how Output Parsers act as a "translator" between the LLM's conversational output and the structured data format required by modern applications.

- Prompt-Driven Entity Extraction

    : I experienced how specific instructions (e.g., defining JSON keys) can significantly improrve the consistency and reliability of entity extraction in specialized fields like Bio-Medicine.

**extract_bio_knowledge()**
1. Code Structure

This function identifies complex biological relationships between entities. I designed it to structure information as (Subject, Relation, Object) triplets, converting unstructured text into machine-readable knowledge data.

2. Technical Decisions

- Knowledge Representation (Triplets)

    : I structured the extraction as (S, R, O) triplets to capture complex medical causalities in a standardized format. This allows the data to be easily extended into a Knowledge Graph and enables logical reasoning.

- System Instruction for Complex Prompts

    : To prevent performance degradation as prompts grow longer, I utilized System Instructions. This clearly separates the "Persona and Rules" from the "Input Data", ensuring consistency even within long contexts.

- Structural Escaping with {{}}

    : I used double braces {{}} to resolve syntax conflicts when requesting JSON formats. This informs the prompt template engine to treat the braces as literal characters rather than variable placeholders.

3. What I Learned

- The Power of Triplets Extraction

    : I learned the fundamentals of Knowledge Graphs by breaking down unstructured text into (S, R, O) structures. I realized how much more valuable this format is compared to raw text.

- How to Architect Long-Form Prompts

    : I learned that assigning a system role significantly increases AI accuracy in complex reasoning compared to just listing commands.

- Beyond Backslashes: Syntax Escaping

    : I discovered that different programming environments have unique ways to escape special characters, specifically mastering the {{}} syntax used in template engines.

### 🧺 utils.py
**save_result_to_json()**
1. Code Structure

This function handles the Data Persistence layer, converting volatile AI-generated data into permanent .json files. It bridges the gap between the execution environment and physical storage for future analysis.

2. Technical Decisions

- Dynamic Filenaming

    : Used strftime("%Y%m%d_%H%M%S") for unique, chronologically sortable identifiers.
    : strftime (String Format Time)

- Cross-Platform Paths

    : Adopted os.path.join to ensure compatibility across different operating systems by handling path separators automatically.

- Global Standardization

    : Forced utf-8 encoding and disabled ensure_ascii to preserve non-English characters and medical symbols. accurately.

3. What I Learned

- Human-Readable Formatting
    
    : Learned how indent=4 improves debugging and data inspection.

- Robustness

    : Realized the importance of verifying directory existence to prevent runtime crashes.

- Pipeline Logic

    : Understood that file I/O is the "connective tissue" between different phases of the project.