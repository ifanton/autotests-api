import pytest
import allure

from http import HTTPStatus

from clients.users.private_users_client import PrivateUserClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema

from fixtures.users import UserFixture

from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTags
from allure_commons.types import Severity

from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake


@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTags.USERS, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
class TestUsers:
    @pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
    @allure.tag(AllureTags.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    @allure.title("Create user")
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):  # Используем фикстуру API клиента
        # Формируем тело запроса на создание пользователя используя Pydantic-схему, подставляется параметризованный домен email
        request = CreateUserRequestSchema(email=fake.email(domain=email))
        # Отправляем запрос на создание пользователя
        response = public_users_client.create_user_api(request)
        # Инициализируем модель ответа на основе полученного JSON в ответе
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # Проверяем статус-код ответа
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что данные ответа совпадают с данными запроса
        assert_create_user_response(request, response_data)
        # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTags.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Get user me")
    def test_get_user_me(
            self,
            function_user: UserFixture,
            private_users_client: PrivateUserClient
    ):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)
        validate_json_schema(response.json(), response_data.model_json_schema())
