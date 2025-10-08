# chat.py

from services.gemini_service import GeminiService
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.live import Live
from rich.spinner import Spinner

# Main function to run the chat application with function calling.
def main():
    """Main function to run the chat application with function calling."""
    console = Console()

    console.print(Panel("🤖 Welcome to SPARC, your AI coding assistant.", title="Welcome", border_style="bold blue"))
    console.print("   Type 'quit' or 'exit' to end the session.", style="bold green")

    try:
        gemini = GeminiService()
        chat_session = gemini.start_chat()

        while True:
            user_input = console.input("[bold cyan]You:[/bold cyan] ").strip()

            if user_input.lower() in ["quit", "exit"]:
                console.print("\nGoodbye! 👋", style="bold red")
                break
            
            if not user_input:
                continue

            # Send the message to the model using a live spinner.
            with Live(Spinner("dots", text="SPARC is thinking..."), console=console, transient=True) as live:
                response = chat_session.send_message(user_input)

            # Print SPARC's response with markdown formatting.
            console.print(Panel(Markdown(response.text), title="SPARC", border_style="bold green", expand=False))
            
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/bold red] {e}")

if __name__ == "__main__":
    main()