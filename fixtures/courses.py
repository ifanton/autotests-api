import pytest
from pydantic import BaseModel

from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.courses.courses_schema import  CreateCourseRequestSchema, CreateCourseResponseSchema

from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture()
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)


@pytest.fixture()  # фикстура создает тестовый курс перед выполнением теста и возвращает объект с данными созданного курса
def function_course(
        courses_client: CoursesClient,  # клиент для работы с API курсов
        function_user: UserFixture,  # пользователь, от имени которого создается курс
        function_file: FileFixture  # загруженный файл, который будет использоваться как превью
) -> CourseFixture:
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)
