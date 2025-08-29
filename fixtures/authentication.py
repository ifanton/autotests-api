import pytest

from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient


@pytest.fixture()  # По умолчанию scope="function" - новый клиент будет создаваться перед каждым тестом
def authentication_client() -> AuthenticationClient:  # Аннотируем возвращаемое значение
    # Создаем новый API клиент для работы с аутентификацией
    return get_authentication_client()
