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

