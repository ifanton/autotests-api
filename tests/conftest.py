import pytest
from pydantic import BaseModel, EmailStr

from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


# Модель для агрегации возвращаемых данных фикстурой function_user
class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:  # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str:  # Быстрый доступ к password пользователя
        return self.request.password


@pytest.fixture()  # По умолчанию scope="function" - новый клиент будет создаваться перед каждым тестом
def authentication_client() -> AuthenticationClient:  # Аннотируем возвращаемое значение
    # Создаем новый API клиент для работы с аутентификацией
    return get_authentication_client()


@pytest.fixture()
def public_users_client() -> PublicUsersClient:
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()


@pytest.fixture()
# Используем фикстуру public_users_client, которая создает нужный API клиент
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    # Формируем тело запроса на создание пользователя используя Pydantic-схему
    request = CreateUserRequestSchema()
    # Отправляем запрос на создание пользователя
    response = public_users_client.create_user(request)
    # Инициализируем модель ответа
    return UserFixture(request=request, response=response)  # Возвращаем все нужные данные
