import ollama
from openai import OpenAI

class JarvisOrchestrator:
    def __init__(self):
        self.local_llm = "llama3" # 8B model optimized for 8GB RAM
        self.client = OpenAI()

    def route_intent(self, prompt):
        # Quick local check for intent
        response = ollama.generate(model=self.local_llm, prompt=f"Is this a system command or a question: {prompt}")
        if "command" in response['response'].lower():
            return "TOOL_EXECUTION"
        return "CLOUD_REASONING"
