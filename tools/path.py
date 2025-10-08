import os

def get_folder_structure(start_path='.'):
    """
    Builds and returns a string representing a clean, visual tree structure of a directory.

    Args:
        start_path (str): The path to the directory to analyze.
                          Defaults to '.' (the current directory).
    
    Returns:
        str: A string containing the formatted directory tree, or an error message.
    """
    if not os.path.isdir(start_path):
        return f"Error: Directory '{start_path}' not found."

    tree_lines = []
    # Use './' for the root if it's the current directory for clarity
    root_display_name = './' if start_path == '.' else os.path.basename(start_path)
    tree_lines.append(root_display_name)

    def generate_tree(directory, prefix=""):
        # Filter out hidden files/directories and sort them for consistent order
        entries = [e for e in os.listdir(directory) if not e.startswith(('.','__'))]
        entries.sort()

        # Use the correct pointer for intermediate vs. last items
        pointers = ['├── '] * (len(entries) - 1) + ['└── ']

        for pointer, entry_name in zip(pointers, entries):
            path = os.path.join(directory, entry_name)
            
            is_dir = os.path.isdir(path)
            # Add a slash to directories for clarity
            display_name = entry_name + '/' if is_dir else entry_name
            tree_lines.append(f"{prefix}{pointer}{display_name}")

            if is_dir:
                # Recursively call for subdirectories with the correct prefix
                extension = '│   ' if pointer == '├── ' else '    '
                generate_tree(path, prefix=prefix + extension)

    # Start the recursive generation
    generate_tree(start_path)
    
    # Join all lines and return the final string
    return "\n".join(tree_lines)

