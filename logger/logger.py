import logging
def setup_logger(log_file):
    # Создаем объект логгера
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Устанавливаем уровень логирования

    # Создаем объект форматирования
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Создаем объект обработчика для записи в файл
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)  # Применяем форматирование к обработчику

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger