import requests
from install_image import install_image


def fetch_epic_nasa_images(nasa_token):
    params = {
        'api_key': nasa_token
    }
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_nasa = response.json()
    for number, epic_image in enumerate(epic_nasa):
        epic_date = epic_image['date'].split()[0]
        url_date = epic_date.replace('-', '/')
        url_image = epic_image['image']
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{url_date}/png/{url_image}.png'
        epic_image['image']
        filepath = f'images/nasa_epic_photo{number}.jpeg'
        install_image(epic_url, filepath, params)


def fetch_nasa_images(nasa_token):
    params = {
        'thumbs': True,
        'count': '5',
        'api_key': nasa_token
    }
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa = response.json()
    for number, launch in enumerate(nasa):
        filepath = f'images/nasa_photo{number}.jpeg'
        install_image(launch['url'],filepath)




