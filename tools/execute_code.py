import subprocess
import shlex

def execute_code(command: str) -> str:
    """
    Executes a shell command and returns its output.

    This function takes a single command as a string, executes it in a
    shell environment, and captures its standard output and standard error.
    It's a secure way to run code, as it executes the command in a separate
    process.

    Args:
        command: A string containing the shell command to be executed.
                 For example: 'ls -l', 'pip install numpy', or 'echo "Hello World"'.

    Returns:
        A string containing the combined standard output and standard error
        from the executed command. If the command runs successfully, this will
        be its output. If the command fails, it will contain the error message.
    """
    if not isinstance(command, str):
        return "Error: Command must be a string."

    try:
        # shlex.split() is used for security to properly handle shell-quoted arguments
        # This helps prevent shell injection attacks.
        args = shlex.split(command)
        
        # Execute the command
        # subprocess.run is a modern and recommended way to run external commands.
        result = subprocess.run(
            args,
            capture_output=True,  # Captures stdout and stderr
            text=True,            # Decodes stdout/stderr as text
            check=False,          # Does not raise an exception on non-zero exit codes
            timeout=60            # Sets a 60-second timeout to prevent long-running processes
        )

        # Combine stdout and stderr for a complete response
        if result.stdout and result.stderr:
            return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        elif result.stdout:
            return result.stdout
        elif result.stderr:
            return result.stderr
        else:
            return "Command executed successfully with no output."

    except FileNotFoundError:
        return f"Error: Command not found. Make sure '{args[0]}' is installed and in your PATH."
    except subprocess.TimeoutExpired:
        return "Error: Command timed out after 60 seconds."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
