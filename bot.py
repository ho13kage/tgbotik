import os
import requests
from bs4 import BeatifulSoup
from telegram import Bot, Update
import time

CHAT_ID = "@proverk1337"
URL = "http://rasp.iek.irk.ru/ScheduleByGroup/32/IEK"

TOKEN = os.getenv("TOKEN")  # Берём токен из переменной окружения
if not TOKEN:
    raise ValueError("Не найден токен! Задайте переменную окружения TOKEN.")
bot = Bot(token=TOKEN)

last_update = ""

def check_schedule():
    global last_update
    response = requests.get(URL)
    soup = BeatifulSoup(response.text, "html.parser")

    schedule_block = soup.find("div", class_="schedule")
    if not schedule_block:
        return
    
    text = schedule_block.get_text(strip=True)

    if text != last_update:
        last_update = text
        bot.send_massage(chat_id=CHAT_ID, text = "Изменения в расписании!!!:\n" + text)


while True:
    check_schedule()
    time.sleep(300)

