import socket  # Импортируем модуль socket для работы с сетевыми соединениями


def server():
    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    '''
    AF_INET — используем IPv4
    SOCK_STREAM — задаем тип сокета как TCP
    '''

    # Привязываем его к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)  #  bind() связывает сокет с определенным IP-адресом и портом

    # Начинаем слушать входящие подключения (максимум 5 в очереди)
    server_socket.listen(5)
    print("Сервер запущен и ждет подключений на localhost:12345 ...")

    while True:  # бесконечный цикл, чтобы сервер всегда ждал новые подключения
        # Принимаем соединение от клиента
        client_socket, client_address = server_socket.accept()
        print(f"Подключение от {client_address}")

        # Получаем данные от клиента
        data = client_socket.recv(1024).decode()
        '''
        recv(1024) ждет и получает данные от клиента, максимум 1024 байта
        .decode() преобразует байты в строку (обычно в UTF-8)
        '''
        print(f"Получено сообщение: {data}")

        # Отправляем ответ клиенту
        response = f"Сервер получил: {data}"
        client_socket.send(response.encode())  # encode() — преобразует строку в байты, так как send() принимает только байты

        # Закрываем соединение только этого клиента, а сервер продолжает работать
        client_socket.close()


if __name__ == '__main__':
    server()
