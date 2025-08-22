"""
{
  "id": "string",
  "title": "string",
  "maxScore": 0,
  "minScore": 0,
  "description": "string",
  "estimatedTime": "string"
}
"""
from pydantic import BaseModel


class CourseSchema(BaseModel):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str

# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id="course-id",
    title="Python API testing",
    maxScore=941,
    minScore=0,
    description="Python API testing automation. Extended course",
    estimatedTime="4 weeks"
)

print('Course default model:', course_default_model)

# Инициализируем модель CourseSchema через распаковку словаря
course_dict = {
    "id": "course-id",
    "title": "Python API testing",
    "maxScore": 941,
    "minScore": 0,
    "description": "Python API testing automation. Extended course",
    "estimatedTime": "4 weeks"
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)
