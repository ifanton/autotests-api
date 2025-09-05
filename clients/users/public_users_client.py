import allure
from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
# CreateUserRequestSchema используется для передачи данных в API, а CreateUserResponseSchema для парсинга ответа
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.routes import APIRoutes


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод выполняет создание нового пользователя

        :param request: Словарь с email, password, lastName, firstName и middleName нового пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            APIRoutes.USERS,
            json=request.model_dump(by_alias=True)  # приводит данные к формату API (например, first_name → firstName)
        )

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)  # безопасный способ загрузки JSON-ответа, исключающий ошибки при работе с необработанными данными

# Добавляем builder для PublicUsersClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом

    :return: Готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())
