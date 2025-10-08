import os

def read_file_content(filepath):
    """
    Reads the entire content of a file and returns it as a string.

    This function uses 'utf-8' encoding, which is a standard for text files.

    Args:
        filepath (str): The full or relative path to the file you want to read.

    Returns:
        str: The content of the file as a single string.
        None: If the file is not found or another error occurs during reading.
    """
    try:
        # The 'with' statement ensures the file is automatically closed
        # even if errors occur.
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file at '{filepath}' was not found. 🤷")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return None