import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# 1. Setup your API Key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file or environment variables.")

genai.configure(api_key=API_KEY)

def list_supported_models():
    print("--- Fetching Available Models ---")
    try:
        # Loop through all models available to your key
        for m in genai.list_models():
            # Filter for models that support generating content (text/chat)
            if 'generateContent' in m.supported_generation_methods:
                print(f"Model ID: {m.name}")
                print(f"  > Display Name: {m.display_name}")
                print(f"  > Description: {m.description}")
                print("-" * 30)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_supported_models()