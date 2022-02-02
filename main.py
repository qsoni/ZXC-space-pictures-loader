from fetch_spacex import fetch_spacex_launch
from fetch_nasa import fetch_epic_nasa_images
from fetch_nasa import fetch_nasa_images
from pathlib import Path
import telegram
import os
import random
import time
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    time_sec = os.getenv('TIME_S')
    bot_id = os.getenv('BOT_ID')
    chat_id = os.getenv('CHAT_ID')
    nasa_token = os.getenv('NASA_TOKEN')

    bot = telegram.Bot(token=bot_id)
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_spacex_launch('images', '66')
    fetch_epic_nasa_images(nasa_token, 'images')
    fetch_nasa_images(nasa_token, 'images')

    while True:
        random_image = random.choice(os.listdir('images'))
        with open(f'images\{random_image}', 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
        bot.send_message(chat_id=chat_id, text="я дед инсайд, мне девять лет, я хочу в психо кидс")
        time.sleep(int(time_sec))


