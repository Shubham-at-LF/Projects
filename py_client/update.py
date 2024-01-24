import requests

endpoint = "http://127.0.0.1:8000/api/product/8/update/"

data = {
    'title' :'you know who',
}

get_response = requests.put(endpoint, json = data) # HTTP request


 
print(get_response.json())

