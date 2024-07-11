#main.py
#print("Hello, Kundan it's your GithubAction Demo Project")
import requests
def call_api():
    url = "https://api.example.com/data"
    response = requests.get(url)
    print(response.json())
    
if __name__ == "__main__":
    call_api()
