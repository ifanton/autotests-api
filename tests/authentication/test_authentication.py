from http import HTTPStatus

import pytest
import allure

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema

from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

from tools.allure.tags import AllureTags
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.authentication
@pytest.mark.regression
@allure.tag(AllureTags.AUTHENTICATION, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    @allure.story(AllureStory.LOGIN)
    @allure.sub_suite(AllureStory.LOGIN)
    @allure.severity(Severity.BLOCKER)
    @allure.title("Login with correct email and password")
    def test_login(
            self,
            function_user: UserFixture,
            authentication_client: AuthenticationClient
    ):
        # Формируем тело запроса на аутентификацию
        request = LoginRequestSchema(
            email=function_user.email,
            password=function_user.password
        )
        # Отправляем запрос на аутентификацию
        response = authentication_client.login_api(request)
        # Инициализируем модель ответа на основе полученного JSON в ответе
        response_data = LoginResponseSchema.model_validate_json(response.text)

        # Выполняем проверку статус-кода
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)  # тест 1
        # Выполняем проверку тела ответа
        assert_login_response(response_data)
        # Выполняем валидацию схемы
        validate_json_schema(response.json(), response_data.model_json_schema())
