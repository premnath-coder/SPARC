# chat.py

from services.gemini_service import GeminiService
import google.generativeai as genai

# Main function to run the chat application with function calling.
def main():
    """Main function to run the chat application with function calling."""
    print("-" * 60)
    print("🤖 Welcome to SPARC. your AI coding assistant.")
    print("   Type 'quit' or 'exit' to end the session.")
    print("-" * 60)

    try:
        gemini = GeminiService()
        chat_session = gemini.start_chat()

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() in ["quit", "exit"]:
                print("\nGoodbye! 👋")
                break
            
            if not user_input:
                continue

            # Send the message to the model.
            # The API will automatically handle the function calling rounds.
            print("\nGemini: Thinking...")
            response = chat_session.send_message(user_input)
            
            # Clear the "Thinking..." line
            # The '\033[F\033[K' is an ANSI escape code to move up and clear the line
            print("\033[F\033[K" + f"Gemini: {response.text}\n")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()