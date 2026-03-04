import requests

url = "https://api.github.com"

response = requests.request(
    method="GET",
    url=url
)

print(response.status_code)
print(response.text)
