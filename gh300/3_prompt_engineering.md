# Prompt Engineering:

- Prompt engineering is how you tell GitHub Copilot what you need with precision and efficiency
- Principles of Prompt Engineering:
    - Single - focus prompt on a single well defined task
    - Specific - instructions are explicit and detailed
    - Short - keep prompts concise and to the point
    - Surround - use descriptive file names and keep related files open

- How Copilot learns:
    - Zero-shot learning
    - One-shot learning
    - Few-shot learning
    - Chain prompting and managing chat history
        - Summarize content

- Role prompting for specialized tasks:
    - Security Export role:
        - "Act as a cybersecurity expert. Create a password validation function that checks for common vulnerabilities and follows OWASP guidelines."
    - Performance Optimization role:
        - "Act as a performance optimization expert. Refactor this sorting algorithm to handle large datasets efficiently."
    - Testing Specialist role:
        - "Act as a testing specialist. Create comprehensive unit tests for this payment processing module, including edge cases and error scenarios."

- Prompt process flow:
    - Inbound flow:
        - Secure prompt transmission and context gathering - https, 
        - Proxy filter
        - Toxicity Filtering - content filtering before proceeding with intent extraction
            - Hate speech and inappropriate content
            - Personal data - filter out PII 
        - Code generation with LLM
    - Outbound flow:
        - Post processing and response validation
            - Code quality
            - Matching public code 
        - Suggestion delivery and feedback loop initiation
            - Grow its knowledge based on accepted suggestions
            - Learn and improve through modifications and rejections of suggestion
    - Repeat for subsequent prompts
    