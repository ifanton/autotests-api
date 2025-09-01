import pytest


# Фикстура, которая будет автоматически вызываться для каждого теста
# Это гарантирует, что данные всегда отправляются в сервис аналитики.
@pytest.fixture(autouse=True)
def send_analytics_data():
    print("\n[AUTOUSE] Отправляем данные в сервис аналитики - фикстура send_analytics_data")


# Фикстура для инициализации настроек автотестов на уровне сессии.
# Вызывается один раз перед выполнением всех тестов в сессии.
# Это важно для подготовки глобальных настроек, которые нужны для всех тестов.
@pytest.fixture(scope="session")
def settings():
    print("\n[SESSION] Инициализируем настройки автотестов - фикстура settings")


# Фикстура для создания данных пользователя, которая будет выполняться один раз на класс тестов
# Это обеспечивает, что данные пользователя создаются один раз и могут быть использованы всеми тестами в этом классе.
@pytest.fixture(scope="class")
def user():
    print("\n[CLASS] Создаем данные пользователя один раз на тестовый класс - фикстура user")


# Фикстура для инициализации API клиента, выполняющаяся для каждого теста.
# Создает новый экземпляр API клиента для изолированного выполнения каждого теста
@pytest.fixture(scope="function")
def users_client():
    print("\n[FUNCTION] Создаем API клиент на каждый автотест - фикстура users_client")


class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        pass

    def test_user_can_logout(self, settings, user, users_client):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        pass
