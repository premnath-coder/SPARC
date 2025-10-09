# tools/available_tools.py

# This dictionary maps the function name (as a string) to the actual function object.
# Our main application will use this to execute the function call.
from tools.convert_mermaid_to_png import mermaid_api_to_png
from tools.execute_code import execute_code
from tools.get_folder_structure import get_folder_structure
from tools.read import read_file_content
from tools.write import write_to_file


TOOL_REGISTRY = {
    "get_folder_structure": get_folder_structure,
    "read_file_content": read_file_content,
    "write_to_file": write_to_file,
    "execute_code": execute_code,
    "convert_mermaid_to_png":mermaid_api_to_png


}