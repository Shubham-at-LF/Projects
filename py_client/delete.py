import requests

endpoint = "http://127.0.0.1:8000/api/product/8/delete/"



get_response = requests.delete(endpoint) # HTTP request


 
print(get_response.status_code)