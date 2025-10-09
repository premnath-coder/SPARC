import requests
import base64

def mermaid_api_to_png(mermaid_code: str, output_path: str):
    """
    Converts a string of Mermaid code to a PNG image using the mermaid.ink API.

    Args:
        mermaid_code (str): A string containing the Mermaid diagram syntax.
        output_path (str): The file path to save the generated PNG image.
    """
    # Encode the Mermaid code in Base64
    code_bytes = mermaid_code.encode("utf-8")
    base64_bytes = base64.b64encode(code_bytes)
    base64_string = base64_bytes.decode("utf-8")

    # Construct the URL
    url = f"https://mermaid.ink/img/{base64_string}"
    
    print("➡️  Requesting diagram from API...")
    try:
        # Make the request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Write the image content to the output file
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"✅ Successfully created PNG at: {output_path}")
        else:
            print(f"❌ API Error: Received status code {response.status_code}")
            print(f"Error details: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: Could not connect to the API. {e}")
