import os
from dotenv import load_dotenv  # Import the function
from config.config import SYSTEM_PROMPT,MODEL_NAME
import google.generativeai as genai
from tools.available_tools import TOOL_REGISTRY

# Load variables from the .env file into the environment
load_dotenv()

class GeminiService:
    """
    A service class to interact with the Google Gemini API,
    configured with function calling tools.
    """
    def __init__(self):
        # Now os.getenv() can read the key loaded from the .env file
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env file or environment variables!")
        
        genai.configure(api_key=api_key)
        

        self.model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            tools=list(TOOL_REGISTRY.values()),
            system_instruction=SYSTEM_PROMPT
        )

    def start_chat(self):
        """Starts a new chat session."""
        return self.model.start_chat(enable_automatic_function_calling=True)
