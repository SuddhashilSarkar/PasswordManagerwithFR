import requests
import json

base_url = "https://pmserver--suddhashil.repl.co"

# Function to register a user
def register_user(username, password):
    url = f"{base_url}/register"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=data)
    return response

# Function to login a user
def login_user(username, password):
    url = f"{base_url}/login"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=data)
    return response

# Example usage
if __name__ == "__main__":
    username = "john_doe"
    password = "foobarbaz"

    # Register a user
    register_response = register_user(username, password)
    print("Registration Response:", register_response.json())

    # Login a user
    login_response = login_user(username, password)
    print("Login Response:", login_response.json())
