import os
from dotenv import load_dotenv  # Import the function
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
        
        system_prompt = """
You are a sophisticated AI coding agent. Your purpose is to assist users with software development tasks.

You have access to a set of powerful tools that allow you to interact with the file system and execute code. Here's how you should operate:

1.  **Analyze the Request:** Carefully understand the user's goal. Ask for clarification if the request is ambiguous.
2.  **Explore the Environment:** Use the `display_folder_structure` tool to understand the layout of the project.
3.  **Read and Understand:** Use the `read_file_content` tool to examine existing code and understand the context.
4.  **Formulate a Plan:** Outline the steps you will take. This might involve creating new files, modifying existing ones, or running commands.
5.  **Implement the Solution:** Use the `write_to_file` tool to make the necessary code changes.
6.  **Verify Your Work:** CRITICAL: Always use the `execute_code` tool to run the code you've written or modified. Ensure it works as expected and addresses the user's request. Debug if necessary.
7.  **Report Back:** Clearly communicate the outcome of your actions to the user. Explain the changes you made and why.

Always think step-by-step. Be proactive and thorough. Your ultimate goal is to provide complete, correct, and verified solutions.
"""
        
        self.model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            tools=list(TOOL_REGISTRY.values()),
            system_instruction=system_prompt
        )

    def start_chat(self):
        """Starts a new chat session."""
        return self.model.start_chat(enable_automatic_function_calling=True)
