import bot_server
import os
import requests
from bs4 import BeatifulSoup
from telegram import Bot, Update
import time

CHAT_ID = "@IEK_RASP_BOT"
URL = "http://rasp.iek.irk.ru/ScheduleByGroup/32/IEK"
TOKEN = "8368418335:AAFaBN0jSnWn2YLVYFXIoLRXVkOB4xSMFuE"
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

