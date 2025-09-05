import logging


def get_logger(name: str) -> logging.Logger:
    # Инициализация логгера с указанным именем
    logger = logging.getLogger(name)
    # Устанавливаем уровень логирования DEBUG для логгера (все уровни от DEBUG и выше)

    logger.setLevel(logging.DEBUG)
    # Создаем обработчик, который будет выводить логи в консоль
    handler = logging.StreamHandler()
    # Устанавливаем уровень логирования DEBUG для обработчика
    handler.setLevel(logging.DEBUG)

    # Задаем форматирование лог-сообщений: включаем время, имя логгера, уровень и сообщение
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    # Применяем форматер к обработчику
    handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(handler)

    # Возвращаем настроенный логгер
    return logger
