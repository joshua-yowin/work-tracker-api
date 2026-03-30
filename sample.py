import requests

url = "https://worktracker-api-joshua123.azurewebsites.net/log"

data = {
    "task": "Test from laptop",
    "time": "now"
}

response = requests.post(url, json=data)
print(response.text)