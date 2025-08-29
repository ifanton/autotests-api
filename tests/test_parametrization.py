import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


# НЕСКОЛЬКО ПАРАМЕТРОВ
@pytest.mark.parametrize("number, expected", [(1, 2), (2, 4), (3, 6)])
def test_several_numbers(number: int, expected: int):
    assert number + number == expected
    assert number * 2 == expected


# ПЕРЕМНОЖЕНИЕ ПАРАМЕТРОВ
@pytest.mark.parametrize("port", ["7070", "8080"])
@pytest.mark.parametrize("host", [
    "http://192.168.185.74",
    "http://192.168.185.15"
])
@pytest.mark.parametrize("os", ["Windows", "Linux"])
def test_multiplication_of_numbers(os: str, host: str, port: str):
    assert len(os + host + port) > 0


# ПАРАМЕТРИЗАЦИЯ ФИКСТУР
@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
# Фикстура будет возвращать три разных хоста
# Соответственно все автотесты использующие данную фикстуру будут запускаться три раза
def host(request: SubRequest) -> str:
    return request.param


# В самом автотесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_host(host: str):
    # Используем фикстуру в автотесте, она вернет нам хост в виде строки
    print(f"\nRunning test on host: {host}")


# ПАРАМЕТРИЗАЦИЯ КЛАССОВ
# Для тестовых классов параметризация указывается для самого класса
@pytest.mark.parametrize("user", ["Alice", "Peter"])
class TestOperations:
    # Параметр "user" передается в качестве аргумента в каждый тестовый метод класса
    @pytest.mark.parametrize("account", ["Credit card", "Debit card"])
    # Параметр "account" передается только в конкретный метод, будет работать "перемножение" параметров
    def test_user_with_operations(self, user: str, account: str):
        print(f"\nUser with operations: {user}, {account}")

    def test_user_without_operations(self, user: str):
        print(f"\nUser without operations: {user}")


# ИДЕНТИФИКАТОРЫ
@pytest.mark.parametrize("phone_number", ["+7-921-000-00-00", "+7-921-000-00-11", "+7-921-000-00-22"])
def test_identifiers_no_ids(phone_number: str):
    pass


# Параметр ids через список строк
@pytest.mark.parametrize(
    "phone_number",
    ["+7-921-000-00-00", "+7-921-000-00-11", "+7-921-000-00-22"],
    ids=[
        "User with money on bank account",
        "User without money on bank account",
        "User with operations on bank account"
    ]
)
def test_identifiers_with_ids_as_list(phone_number: str):
    pass


# Параметр ids через кортеж строк
@pytest.mark.parametrize("points", [0, 100], ids=("Min", "Max"))
def test_identifiers_with_ids_as_tuple(points):
    pass

# Словарь пользователей: номер телефона — ключ, описание — значение
users = {
    "+7-921-000-00-00": "User with money on bank account",
    "+7-921-000-00-11": "User without money on bank account",
    "+7-921-000-00-22": "User with operations on bank account"
}


@pytest.mark.parametrize(
    "phone_number",
    users.keys(),  # Передаем список номеров телефонов
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"  # Генерируем идентификаторы динамически
)
def test_identifiers_with_dynamic_ids(phone_number: str):
    pass
