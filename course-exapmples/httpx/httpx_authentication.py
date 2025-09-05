import httpx
import os


os.environ["NO_PROXY"] = "*"  # отключение прокси

# Данные для входа в систему
login_payload = {
  "email": "panteleev@example.com",
  "password": "P@ssw0rd"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response status code:", login_response.status_code)
print("Login response:",login_response_data)

# Формируем payload для обновления токена
refresh_payload = {
  "refreshToken": login_response_data['token']['refreshToken']
}

# Выполняем запрос на обновление токена
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

# Выводим обновленные токены
print("Refresh response status code:", refresh_response.status_code)
print("Refresh response:", refresh_response_data)
