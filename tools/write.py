import os

def write_to_file(filepath, content):
    """
    Writes a string of content to a specified file.

    If the file exists, its original content will be overwritten.
    If the file or directory does not exist, it will be created.

    Args:
        filepath (str): The full or relative path for the file to be created.
        content (str): The string data you want to write to the file.

    Returns:
        bool: True if the file was written successfully, False otherwise.
    """
    try:
        # The 'with' statement ensures the file is properly handled and closed.
        # 'w' is the mode for writing. It overwrites existing files.
        # 'encoding='utf-8'' is a best practice for text files.
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"An error occurred while writing to '{filepath}': {e} ❌")
        return False