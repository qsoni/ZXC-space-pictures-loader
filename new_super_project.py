import requests
import datetime
from os.path import splitext
from pprint import pprint
from pathlib import Path
from urllib.parse import urlparse
import telegram
import os
import random

random_image = random.choice(os.listdir('images'))

bot = telegram.Bot(token='5023274041:AAF-Hqol0GIXDYTknbgv4Ts76lWnTbGRUP0')
bot.send_message(chat_id='@deadinsidamsyda', text="я дед инсайд, мне девять лет, я хочу в психо кидс")
bot.send_document(chat_id='@deadinsidamsyda', document=open(f'images\{random_image}', 'rb'))

def install_images(link, filename, params=''):
    url = link
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def epic_nasa_images():
    params = {
        'api_key': 'NjCIHo8fhBS3PyclGht8EtBbe2VGrJoK9jk2dh4e'
    }
    q = 0
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_nasa = response.json()
    for epic_image in epic_nasa:
        epic_date = epic_image['date'].split()[0]
        url_date = epic_date.replace('-', '/')
        url_image = epic_image['image']
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{url_date}/png/{url_image}.png'
        epic_image['image']
        q = q + 1
        filename_two = f'images/nasa_epic_photo{q}.jpeg'
        params = {
            'api_key': 'NjCIHo8fhBS3PyclGht8EtBbe2VGrJoK9jk2dh4e'
        }
        install_images(epic_url, filename_two, params)




def picture_resolution():
    your_link = 'https://apod.nasa.gov/apod/image/2111/NGC3314_HubbleOstling_960.jpg'
    o = urlparse(your_link)
    y = splitext(o.path)[1]
    print(y)



def nasa_images():
    params = {
        'thumbs': True,
        'count': '5',
        'api_key': 'NjCIHo8fhBS3PyclGht8EtBbe2VGrJoK9jk2dh4e'
    }
    z = 0
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa = response.json()
    for nasa_image in nasa:
        nasa_url = nasa_image['url']
        z = z + 1
        filename_one = f'images/nasa_photo{z}.jpeg'
        install_images(nasa_url, filename_one)



def fetch_spacex_last_launch():
    links_num = 0
    url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url)
    links = response.json()[66]['links']['flickr_images']
    for link in links:
        links_num = links_num + 1
        filename = f'images/spacex_photo{links_num}.jpeg'
        install_images(link, filename)


Path("images").mkdir(parents=True, exist_ok=True)
nasa_images()
epic_nasa_images()
picture_resolution()
fetch_spacex_last_launch()







