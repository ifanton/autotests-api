// Создаём подключение к WebSocket-серверу по адресу ws://localhost:8765
const websocket = new WebSocket("ws://localhost:8765");

websocket.onopen = () => {
  console.log("Соединение установлено");
  websocket.send("Привет, сервер!");
};

// Добавляем обработчик входящих сообщений от сервера
websocket.onmessage = (message) => {
  console.log("Сообщение от сервера:", message.data);
};

websocket.onclose = () => {
  console.log("Соединение закрыто");
};
