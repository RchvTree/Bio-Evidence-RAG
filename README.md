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