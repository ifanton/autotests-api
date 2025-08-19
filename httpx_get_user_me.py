import httpx
import os


os.environ["NO_PROXY"] = "*"  # отключение прокси

login_payload = {
  "email": "panteleev@example.com",
  "password": "P@ssw0rd"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

accessToken = login_response_data['token']['accessToken']

headers = {
    "Authorization": f"Bearer {accessToken}"
}

get_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
get_me_response_data = get_me_response.json()

print('Get me response status code:', get_me_response.status_code)
print('Get me response data:', get_me_response_data)
