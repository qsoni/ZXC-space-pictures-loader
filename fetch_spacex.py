import requests
from install_image import install_image


def fetch_spacex_last_launch():
    links_num = 0
    url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()[66]['links']['flickr_images']
    for number, launch in enumerate(links):
        filename = f'images/spacex_photo{number}.jpeg'
        install_image(launch, filename)


