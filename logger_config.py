import logging

def setup_logger():
    logger = logging.getLogger('pytest_logger')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('test.log')
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)  # Пример: выводить в консоль только ошибки

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger