from typing import Any


def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому

    :param actual: Фактический статус-код
    :param expected: Ожидаемый статус-код
    :raises AssertionError: Если статус-коды не совпадают
    """
    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected status code: {expected} '
        f'Actual status code: {actual}'
    )

def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому

    :param actual: Фактическое значение
    :param expected: Ожидаемое значение
    :param name: Название проверяемого значения
    :raises AssertionError: Если значения не совпадают
    """
    assert actual == expected, (
        f'Incorrect value: "{name}" '
        f'Expected value: {expected} '
        f'Actual value: {actual}'
    )

def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным

    :param actual: Фактическое значение
    :param name: Название проверяемого значения
    :raises AssertionError: Если фактическое значение ложно
    """
    assert actual, (
        f'Incorrect value: "{name}" '
        f'Expected true value but got: {actual}'
    )
