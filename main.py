import logging
from datetime import datetime


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')          # Налаштування логування


now = datetime.now()          # Отримуємо поточну дату
year = now.year
month = now.month
day = now.day


logging.info("Сьогоднішня дата: {}-{}-{}".format(year, month, day))          # Виводимо повідомлення через logging
