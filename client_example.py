import os
import sys
import requests

def main():
    # Replace with the Base URL output from your Colab notebook
    base_url = os.environ.get("COLAB_BASE_URL", "https://YOUR-NGROK-SUBDOMAIN.ngrok-free.app")
    api_key = os.environ.get("COLAB_API_KEY", "sk-colab-your-generated-key")

    endpoint = f"{base_url.rstrip('/')}/v1/chat/completions"
    
    payload = {
        "model": "colab-runner",
        "messages": [
            {"role": "system", "content": "You are a concise, helpful programming assistant."},
            {"role": "user", "content": "Write a Python function to check if a string is a palindrome."}
        ],
        "temperature": 0.6,
        "max_tokens": 256
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    print(f"Connecting to: {endpoint} ...")
    try:
        response = requests.post(endpoint, json=payload, headers=headers, timeout=120)
        response.raise_for_status()
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        print("\n--- Model Response ---")
        print(content)
        print("----------------------")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        if hasattr(e, 'response') and e.response is not None:
            print(f"Status code: {e.response.status_code}", file=sys.stderr)
            print(f"Response body: {e.response.text}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
