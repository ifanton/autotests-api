import allure
from httpx import Response

from clients.api_client import APIClient

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import GetExercisesQuerySchema, GetExerciseResponseSchema, \
    GetExercisesResponseSchema, CreateExerciseRequestSchema, UpdateExerciseRequestSchema, CreateExerciseResponseSchema, \
    UpdateExerciseResponseSchema
from tools.routes import APIRoutes


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий для определенного курса

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(APIRoutes.EXERCISES, params=query.model_dump(by_alias=True))

    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании по идентификатору

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления задания по идентификатору

        :param exercise_id: Идентификатор задания
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"{APIRoutes.EXERCISES}/{exercise_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод, который будет запрашивать задание по идентификатору и возвращать JSON-структуру

        :param exercise_id: Идентификатор задания
        :return: JSON-структура задания
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод, который будет запрашивать список заданий и возвращать JSON-структуру

        :param query: Словарь c courseId
        :return: JSON-структура заданий курса
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод, который будет создавать задание и возвращать JSON-структуру

        :param request: Словарь CreateExerciseRequestDict
        :return: JSON-структура созданного задания
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Метод, который будет обновлять задание и возвращать JSON-структуру

        :param exercise_id: Идентификатор задания
        :param request: Словарь UpdateExerciseRequestDict
        :return: JSON-структура обновленного задания
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

# Добавляем builder для ExercisesClient
def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом

    :return: Готовый к использованию ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))
