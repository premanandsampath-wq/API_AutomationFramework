import requests 

def test_basic_api():
    url = "https://dummyjson.com/products/1"
    response = requests.get(url)
    if response.status_code == 200: 
        print("API call successful!")
        print("response:", response.json()) 
        print("response status code:", response.status_code)
    return 

#if __name__ == "__main__":
 #   test_basic_api()