from telethon import TelegramClient
from main import get_current_date, get_congrats, get_employees, truncate_date
from time import sleep
from random import choice
from decouple import config


api_id = config('api_id')
api_hash = config('api_hash')


async def main(msg_to_chat):
    await client.send_message("test_happy_birthday", msg_to_chat)


if __name__ == '__main__':
    client = TelegramClient('anon', api_id, api_hash)
    client.start()
    current_date = get_current_date()
    employee_congrats = list()
    employees = get_employees()
    for employee in employees:
        if truncate_date(employee['Birthday']) == current_date:
            employee_congrats.append(employee)
    congrats = get_congrats()
    for employee in employee_congrats:
        congrat = choice(congrats)
        client.loop.run_until_complete(main(f"{employee['Name']}, {congrat[0]}"))
        sleep(30)
