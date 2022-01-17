from fetch_spacex import fetch_spacex_last_launch
from fetch_nasa import epic_nasa_images
from fetch_nasa import nasa_images
from os.path import splitext
from pathlib import Path
from urllib.parse import urlparse
import telegram
import os
import random
import time
from dotenv import load_dotenv


if __name__ == '__main__':
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch
    epic_nasa_images()
    nasa_images()

    load_dotenv()
    time_sec = os.getenv('TIME_S')
    bot_id = os.getenv('BOT_ID')
    chat_id = os.getenv('CHAT_ID')

    bot = telegram.Bot(token=bot_id)

    while True:
        random_image = random.choice(os.listdir('images'))
        bot.send_document(chat_id=chat_id, document=open(f'images\{random_image}', 'rb'))
        bot.send_message(chat_id=chat_id, text="я дед инсайд, мне девять лет, я хочу в психо кидс")
        time.sleep(int(time_sec))


