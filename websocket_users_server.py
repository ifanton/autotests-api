import asyncio  # Импортируем asyncio для работы с асинхронными операциями

import websockets  # Импортируем библиотеку для работы с WebSockets
from websockets import ServerConnection


# Обработчик входящих сообщений
async def users_echo(websocket: ServerConnection):  # websocket: ServerConnection — это объект соединения с клиентом
    async for message in websocket:  # Асинхронно обрабатываем поток входящих сообщений
        print(f"Получено сообщение от пользователя: {message}")
        response = f"Сообщение пользователя: {message}" # Формируем ответное сообщение

        for i in range(1, 6):
            numbered_response = f"{i} {response}"
            await websocket.send(numbered_response)  # Отправляем ответ клиенту


# Запуск Websocket-сервера на порту 8765
async def main():
    server = await websockets.serve(users_echo, "localhost", 8765)  # Запускаем сервер, который слушает соединения на localhost:8765 и использует echo в качестве обработчика сообщений
    print("Websocket-сервер запущен на ws://localhost:8765")
    await server.wait_closed()  # Ожидаем закрытия сервера (обычно он работает вечно)


asyncio.run(main())  # Запускаем асинхронный код
