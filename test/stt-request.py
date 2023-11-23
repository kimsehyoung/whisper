import requests
import time
import json

url = "http://localhost:8000/speech/translation"

headers = {
    "Content-Type": "application/json",
}

with open("stt-request.json", "r") as body:
    data = json.load(body)

start_time = time.time()
for _ in range(1):
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code, response.text)

end_time = time.time()
total_time = end_time - start_time
print(f"STT elapsed time: {total_time:.2f} seconds")


