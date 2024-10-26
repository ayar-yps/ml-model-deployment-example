import requests

url = "http://localhost:9696/predict"

customer_data = {"job": "management", "duration": 400, "poutcome": "success"}

response = requests.post(url, json=customer_data).json()

print(response)