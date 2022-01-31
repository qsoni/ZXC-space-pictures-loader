import requests


def install_image(link, filename, params=''):
    response = requests.get(link, params=params)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)