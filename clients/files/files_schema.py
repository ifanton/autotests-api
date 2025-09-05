from pydantic import BaseModel, Field, HttpUrl, FilePath

from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Описание структуры файла
    """
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid()}.png")
    directory: str = Field(default="tests") # Директорию оставляем статичной, чтобы все тестовые файлы на сервере попадали в одну папку
    upload_file: FilePath  # Директорию, откуда берем загружаемый файл указываем вручную


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла
    """
    file: FileSchema


class GetFileResponseSchema(BaseModel):
    """
    Описание структуры запроса получения файла.
    """
    file: FileSchema
