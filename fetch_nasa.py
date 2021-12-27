import requests
from dotenv import load_dotenv
import os
from pathlib import Path

def install_images(link, filename, params=''):
    url = link
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def epic_nasa_images():
    params = {
        'api_key': nasa_token
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
            'api_key': nasa_token
        }
        install_images(epic_url, filename_two, params)


def nasa_images():
    params = {
        'thumbs': True,
        'count': '5',
        'api_key': nasa_token
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

Path("images").mkdir(parents=True, exist_ok=True)
load_dotenv()
nasa_token = os.getenv('NASA_TOKEN')