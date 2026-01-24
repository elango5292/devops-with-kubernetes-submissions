import os
import requests

def get_rand_wiki_url():
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyTestBot/1.0; +https://example.com)"
    }
    r = requests.get("https://en.wikipedia.org/wiki/Special:Random", headers=headers)
    url = r.url
    print("Random wiki URL: " ,url)
    return url

def create_wiki_todo():
    todo_content = get_rand_wiki_url()
    # Use environment variable or valid default within the cluster
    backend_url = os.getenv("TODO_BACKEND_URL", "http://todo-backend-svc:2345")

    print(f"Sending todo to: {backend_url}/todos")
    response = requests.post(f"{backend_url}/todos", json={"todo": f"Read {todo_content}"})

    if response.status_code == 200:
        print("message: Todo added successfully")
    else:
        print(f"ERROR: Failed to add todo. Status: {response.status_code}, Body: {response.text}")

if __name__ == "__main__":
    try:
        create_wiki_todo()
    except Exception as e:
        print (f"ERROR: {e}" )
