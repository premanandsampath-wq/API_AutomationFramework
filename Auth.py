import requests

def main():
    url = "https://dummyjson.com/auth/login"
    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    response = requests.post(url, json=payload)

    print("Status:", response.status_code)
    print("Body:", response.json())

if __name__ == "__main__":
    main()