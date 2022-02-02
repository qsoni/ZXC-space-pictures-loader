import requests
from install_image import install_image


def fetch_spacex_launch(filepath, launch_number):
    url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()[launch_number]['links']['flickr_images']
    for number, launch in enumerate(links):
        install_image(launch, f'{filepath}/spacex_photo{number}.jpeg')


