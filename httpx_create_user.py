import httpx
import os
from tools.fakers import get_random_email


os.environ["NO_PROXY"] = "*"  # отключение прокси

payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())
