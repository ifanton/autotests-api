"""
{
  "id": "string",
  "title": "string",
  "maxScore": 0,
  "minScore": 0,
  "description": "string",
  "previewFile": {
    "id": "string",
    "filename": "string",
    "directory": "string",
    "url": "https://example.com/"
  },
  "estimatedTime": "string",
  "createdByUser": {
    "id": "string",
    "email": "user@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
  }
}
"""
import uuid

from pydantic import BaseModel, ConfigDict, Field, EmailStr, HttpUrl, ValidationError
from pydantic.alias_generators import to_camel

from tools.fakers import fake


# Добавим модель FileSchema
class FileSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    url: HttpUrl = None
    filename: str = None
    directory: str = None


class UserSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr = get_random_email()
    last_name: str = None
    first_name: str = None
    middle_name: str = None

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Python API testing"
    max_score: int = Field(default=941)
    min_score: int = Field(default=0)
    description: str = "Python API testing automation. Extended course"
    preview_file: FileSchema = None # Вложенный объект для файла-превью
    estimated_time: str = Field(default="4 weeks")
    created_by_user: UserSchema = None  # Вложенный объект для пользователя, создавшего курс


# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id="course-id",
    title="Python API testing",
    maxScore=941,
    minScore=0,
    description="Python API testing automation. Extended course",
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses"
    ),
    estimatedTime="4 weeks",
    createdByUser=UserSchema(
        id="user-id",
        email="user@email.com",
        lastName="Bond",
        firstName="James",
        middleName="007"
    )
)

print('Course default model:', course_default_model)

# Инициализируем модель CourseSchema через распаковку словаря
course_dict = {
    "id": "course-id",
    "title": "Python API testing",
    "maxScore": 941,
    "minScore": 0,
    "description": "Python API testing automation. Extended course",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "4 weeks",
    "createdByUser": {
        "id": "user-id",
        "email": "user@email.com",
        "lastName": "Bond",
        "firstName": "James",
        "middleName": "007"
    }
}

course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)
print('Course dict model JSON:', course_dict_model.model_dump(by_alias=True))

# Инициализируем модель CourseSchema через JSON
course_json = """
{
    "id": "course-id",
    "title": "Python API testing",
    "maxScore": 941,
    "minScore": 0,
    "description": "Python API testing automation. Extended course",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "4 weeks",
    "createdByUser": {
        "id": "user-id",
        "email": "user@email.com",
        "lastName": "Bond",
        "firstName": "James",
        "middleName": "007"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)  # парсим строку и создаем объект CourseSchema
print('Course JSON model:', course_json_model)

# Инициализируем модели CourseSchema без передачи конкретных параметров (они уже заданы по умолчанию)
course1 = CourseSchema()
course2 = CourseSchema()
print('Default course JSON:',course1.model_dump(by_alias=True))
print('Default course JSON:',course2.model_dump(by_alias=True))

try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses",
    )
except ValidationError as error:
    print(error)
    print(error.errors())
