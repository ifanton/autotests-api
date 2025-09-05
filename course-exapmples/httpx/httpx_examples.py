import httpx
import os


os.environ["NO_PROXY"] = "*"  # отключение прокси

# 1. Основные функции HTTPX
# Отправка GET-запроса
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)
print(response.json())  # response.json() — парсит JSON-ответ

# Отправка POST-запроса
data = {
    "title": "new task",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)  # json=data автоматически сериализует Python-словарь в JSON

print(response.status_code)
print(response.json())

# Отправка данных в application/x-www-form-urlencoded
data = {"username": "test_user", "password": "123456"}

response = httpx.post("https://httpbin.org/post", data=data)

print(response.json())

# Передача заголовков
headers = {"Authorization": "Bearer my_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.json())

# Работа с параметрами запроса
params = {"userId": 2}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)  # params добавляет параметры к URL, аналогично ?key=value

print(response.url)
print(response.json())

# Отправка файлов
files = {"file": ("example.txt", open("example.txt", "rb"))}

response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())

# 2. Работа с сессиями
# Использование httpx.Client (позволяет не устанавливать новое соединение для каждого запроса)
with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())
print(response2.json())

# Добавление базовых заголовков в Client
client = httpx.Client(headers={"Authorization": "Bearer my_token"})  # клиент автоматически добавляет Authorization ко всем запросам

response = client.get("https://httpbin.org/get")

print(response.json())
client.close()

# 3. Работа с ошибками
# Проверка статуса ответа (raise_for_status)
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
    print(response.status_code)
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

# Обработка таймаутов
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)  # если сервер отвечает более 2 секунд, запрос прервется
    print(response.status_code)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")

# 4. Дополнительно
# Поддержка HTTP/2
client = httpx.Client(http2=True)

response = client.get("https://www.google.com")

print(response.http_version)
