from httpx import Client

from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict

from typing import TypedDict


class AuthenticationUserDict(TypedDict):
    """
    Описание структуры данных пользователя для аутентификации
    """
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя

    :param user: Объект AuthenticationUserDict с email и password пользователя
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization
    """
    authentication_client = get_authentication_client()  # Инициализируем AuthenticationClient для аутентификации

    # Инициализируем запрос на аутентификацию
    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    # Выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )
