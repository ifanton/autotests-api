import asyncio

import websockets


async def users_client():
    uri = "ws://localhost:8765"  # Адрес WebSocket-сервера
    async with websockets.connect(uri) as websocket:  # Устанавливаем соединение с сервером, используем async with, чтобы соединение автоматически закрылось после завершения работы клиента
        message = "Привет, сервер!"  # Сообщение, которое отправит клиент
        print(f"Отправка: {message}")
        await websocket.send(message)  # Асинхронно отправляем сообщение серверу

        for _ in range(5):
            response = await websocket.recv()  # Асинхронно получаем ответ от сервера
            print(response)


asyncio.run(users_client())  # Запускаем асинхронную функцию клиента
