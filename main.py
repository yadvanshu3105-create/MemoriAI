import os
from google import genai

# Initialize the Google GenAI client (uses free tier/environment key)
client = genai.Client()

def chat(query):
    # Using a fast, free-tier friendly model
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=query,
    )
    return response.text

if __name__ == "__main__":
    print("MemoriAI Engine Initialized with Google AI.")
    query = input("Query: ")
    print(chat(query))
    
