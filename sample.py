import requests

url = "https://worktracker-api-joshua123-hzd0fzepcpb9cuec.centralindia-01.azurewebsites.net/log"
data = {
    "task": "Test from laptop",
    "time": "now"
}
response = requests.post(url, json=data)
print(response.text)