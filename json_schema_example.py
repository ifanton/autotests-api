from jsonschema import validate, ValidationError


# Пример схемы
schema = {
    "type": "object",
    "properties": {
        "name": { "type": "string" },
        "age": { "type": "number" }
    },
    "required": ["name"]
}

# Пример данных
data = {
    "name": "Anton",
    "age": "39"
}

try:
    validate(instance=data, schema=schema)
    print("Данные соответствуют схеме")
except ValidationError as e:
    print(f"Ошибка валидации: {e.message}")
