import requests

url = "https://httpbin.org/headers"

response = requests.request(
    method="GET",
    url=url
)

print(response.status_code)
print(response.text)
