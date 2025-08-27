import pytest


# def test_first_try():
#     greeting = "Hello"
#     assert greeting == "HELLO"
#
# def test_second_try():
#     print("World!")
#
# def test_assert_positive_case():
#     assert (1 + 1) == 2  # Ожидается, что тест пройдет
#
# def test_assert_negative_case():
#     assert (1 + 1) == 3, "Сумма 1 и 1 должна быть 2!"  # Тут должна быть ошибка
#
# def test_in_list():
#     assert 3 in [1, 2, 3, 4]
#
# def test_lists():
#     assert [1, 2, 3] == [1, 2, 4]
#
# def test_boolean():
#     is_authenticated = True
#     assert is_authenticated
#
# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         1 / 0
#
#
# class TestClass:
#     def test_class_function(self):
#         assert 1 == 1

@pytest.mark.smoke
class TestLogin:
    @pytest.mark.smoke
    def test_valid_login(self):
        pass

    @pytest.mark.regression
    def test_invalid_login(self):
        pass

@pytest.mark.regression
class TestRegistration:
    @pytest.mark.regression
    def test_valid_registration(self):
        pass

    @pytest.mark.smoke
    def test_invalid_registration(self):
        pass

@pytest.mark.smoke
@pytest.mark.regression
class TestCheckout:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_checkout(self):
        pass

    def test_invalid_checkout(self):
        pass

def test_search():
    pass