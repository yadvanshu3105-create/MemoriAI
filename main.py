import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key="YOUR_ACTUAL_API_KEY_HERE"
)

class MemoriAIAssistant:
    def __init__(self):
        # Local structured memory cache
        self.memory_store = [
            "User is working on a hackathon project named MemoriAI.",
            "Target architecture leverages NVIDIA Nemotron-4 340B on Nebius Cloud."
        ]

    def retrieve_memories(self, query: str) -> str:
        """Simulates selective memory retrieval for prompt injection."""
        relevant = [m for m in self.memory_store if any(k in m.lower() for k in query.lower().split())]
        return "\n".join(relevant) if relevant else "No prior context found."

    def chat(self, user_query: str):
        retrieved_context = self.retrieve_memories(user_query)
        
        system_prompt = (
            "You are MemoriAI, a private virtual assistant equipped with dynamic long-term memory retrieval.\n"
            f"Retrieved User Memories:\n{retrieved_context}"
        )

        response = client.chat.completions.create(
            model="nvidia/nemotron-4-340b-instruct",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content

if __name__ == "__main__":
    assistant = MemoriAIAssistant()
    print("MemoriAI Engine Initialized.")
    query = "What model and architecture is MemoriAI running on?"
    print(f"Query: {query}")
    print("Response:", assistant.chat(query))
    
