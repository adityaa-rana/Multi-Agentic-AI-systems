import os

def get_openai_api_key():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY not found. Did you load .env?")
    return key

def get_serper_api_key():
    key = os.getenv("SERPER_API_KEY")
    if not key:
        raise ValueError("SERPER_API_KEY not found. Did you load .env?")
    return key
def pretty_print_result(result):
    print("----- RESULT -----")
    print(result)
    print("------------------")
