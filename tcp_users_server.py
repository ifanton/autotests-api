import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("Сервер запущен ...")

    # Список для хранения истории сообщений
    messages: list[str] = []

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        # Получаем данные от клиента
        message = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {message}")

        # Записываем историю сообщений в список
        messages.append(message)

        # Отправляем историю сообщений клиенту
        client_socket.send('\n'.join(messages).encode())

        client_socket.close()


if __name__ == '__main__':
    server()
