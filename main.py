import logging

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

try:
    x = 10 / 0
except Exception as e:
    logging.error("Виникла помилка: " + str(e))
