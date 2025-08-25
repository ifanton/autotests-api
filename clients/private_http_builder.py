from httpx import Client

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema

from pydantic import BaseModel, EmailStr


class AuthenticationUserSchema(BaseModel):
    """
    Описание структуры данных пользователя для аутентификации
    """
    email: EmailStr
    password: str


def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя

    :param user: Объект AuthenticationUserDict с email и password пользователя
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization
    """
    authentication_client = get_authentication_client()  # Инициализируем AuthenticationClient для аутентификации

    # Инициализируем запрос на аутентификацию
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    # Выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )
