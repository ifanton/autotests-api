import uuid

from pydantic import BaseModel, Field, EmailStr

from tools.fakers import fake


class UserPersonalInfoSchema(BaseModel):  # сначала выделяем вложенные сущности
    first_name: str = None   # Значение по умолчанию
    middle_name: str = None
    last_name: str = None
    age: int = None
    family_status: str = Field(
        default=None,
        alias="familyStatus"  # для поля задан псевдоним и значение по умолчанию
    )


class ShortUserSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))  # генерация случайного значения uuid
    email: EmailStr = get_random_email()  # используем функцию и валидацию формата через отдельный тип pydantic


class ExtendedUserSchema(ShortUserSchema):
    personal_info: UserPersonalInfoSchema = None  # Вложенная модель, значение по умолчанию None
    is_active: bool = True  # значение по умолчанию True


# Инициализируем модель (создаем экземпляр класса ExtendedUserSchema) через передачу аргументов
user = ExtendedUserSchema(
    id="10cff3c0-17ae-46f6-8bfe-ce3d4ab3adf8",
    email="email@example.com",
    personal_info=UserPersonalInfoSchema(
        first_name="Anton",
        middle_name="Sergeevich",
        last_name="Panteleev",
        age="39",  # числовое значение задано в виде строки
        familyStatus="married"
    ),
    is_active=False  # переопределяем значение на False
)

user1 = ExtendedUserSchema()

print('User:', user)  # Вывод всего объекта user
print('User email:', user.email)  # Вывод значения параметра email
print('User age:', user.personal_info.age)  # строка "39" автоматически преобразована в тип int
print('User dict:', user.personal_info.model_dump())  # Выводит как словарь
print('User JSON:', user.personal_info.model_dump_json(by_alias=True))  # Выводит как JSON-строку c alias

print('User1:', user1)
