import ollama

class Orchestrator:
    def route_intent(self, user_input):
        # Local intent routing via Llama 3 8B
        response = ollama.chat(model='llama3', messages=[
            {'role': 'system', 'content': 'Classify intent: [VISION, AUTOMATION, KNOWLEDGE, MUSIC]'},
            {'role': 'user', 'content': user_input}
        ])
        return response['message']['content']
