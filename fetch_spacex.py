import requests
from pathlib import Path

def install_image(link, filename, params=''):
    response = requests.get(link, params=params)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    links_num = 0
    url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url)
    links = response.json()[66]['links']['flickr_images']
    for link in links:
        links_num = links_num + 1
        filename = f'images/spacex_photo{links_num}.jpeg'
        install_image(link, filename)

Path("images").mkdir(parents=True, exist_ok=True)