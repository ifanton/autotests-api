from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel

from tools.fakers import fake


class UserSchema(BaseModel):
    """
    Модель пользователя
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class CreateUserRequestSchema(BaseModel):
    """
    Модель запроса на создание пользователя
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr = get_random_email()
    password: str = "p@ssw0rd"
    last_name: str = "string"
    first_name: str = "string"
    middle_name: str = "string"


class CreateUserResponseSchema(UserSchema):
    """
    Модель ответа на создание пользователя
    """
    user: UserSchema

create_response = CreateUserRequestSchema()
print(create_response)
