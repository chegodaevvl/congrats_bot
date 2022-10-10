import telebot
from decouple import config
import gspread
from datetime import datetime
from random import choice
from time import sleep


happy_birthday_bot = telebot.TeleBot(config('bot_uid'))
chat_title = f"@{config('test_happy_birthday')}"
gs_session = gspread.service_account(filename=config('google_token_filename'))
gs_table = gs_session.open('google_table_title')


def get_current_date() -> str:
    """
        Функция, возвращающая в строковом формате текущую дату и месяц
    :return: дата и месяц, разделенные точкой
    """
    current_date = datetime.now()
    return f'{current_date.day}.{current_date.month}'


def get_employees() -> list:
    """
        Функция получения списка сотрудников из google таблицы
    :return: список словарей, каждый словарь - описание сотрудника
    """
    employees_sheet = gs_table.worksheet("google_employees")
    return employees_sheet.get_all_records()


def get_congrats() -> list:
    """
        Функция получения списка поздравлений
    :return: Список поздравлений
    """
    congrats_sheet = gs_table.worksheet("google_congrats")
    return congrats_sheet.get_all_values()


def truncate_date(some_date: str) -> str:
    """
        Функция усечения даты до дня и месяца
    :param some_date: дата в строковом виде, с разделителем '/'
    :return: дата и месяц, разделенные точкой
    """
    day, month, year = map(int, some_date.split('/'))
    return f'{day}.{month}'


if __name__ == '__main__':
    current_date = get_current_date()
    employee_congrats = list()
    employees = get_employees()
    for employee in employees:
        if truncate_date(employee['Birthday']) == current_date:
            employee_congrats.append(employee)
    congrats = get_congrats()
    for employee in employee_congrats:
        congrat = choice(congrats)
        happy_birthday_bot.send_message(chat_title, f"{employee['Name']}, {congrat[0]}")
        sleep(30)
