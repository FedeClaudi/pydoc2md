import requests


def check_url(url):
    request = requests.get(url)
    if request.status_code == 200:
        return True
    else:
        return False
