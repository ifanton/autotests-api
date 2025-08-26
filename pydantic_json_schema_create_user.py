from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user_api(create_user_request)  # Используем метод create_user_api так как нужен объект Response, а не модель CreateUserResponseSchema
create_user_response_json = create_user_response.json()
create_user_response_schema = CreateUserResponseSchema.model_json_schema()  # Получаем JSON-схему из Pydantic-модели ответа

# del create_user_response_json['user']['middleName']
# create_user_response_json['user']['email'] = "HELLO"
# create_user_response_json['user']['middleName'] = 3

# Проверяем, что JSON-ответ от API соответствует ожидаемой JSON-схеме
validate_json_schema(instance=create_user_response_json, schema=create_user_response_schema)
