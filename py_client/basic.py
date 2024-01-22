import requests

#endpoint = "http://httpbin.org/status/200/"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint,json = {"query": "hello world Jai Shri RAM"}) # HTTP request

# print(get_response.text)
# print(get_response.status_code)

print(get_response.json())

# normal http request gives html 
# but api http request give json object 