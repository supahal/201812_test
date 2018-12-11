import requests
import json

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

from lib.constants import BASE_URL

AUTHOR_URL = urljoin(BASE_URL, 'authors')
BOOK_URL = urljoin(BASE_URL, 'books')


def get_author():
    response = requests.get(AUTHOR_URL)
    if response.ok:
        return response
    else:
        return None


def get_book():
    response = requests.get(BOOK_URL)
    if response.ok:
        return response
    else:
        return None


def post_author(data={}):
    response = requests.post(AUTHOR_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    if response.ok:
        return response
    else:
        return None


def post_book(data={}):
    response = requests.post(BOOK_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    if response.ok:
        return response
    else:
        return None


def put_author(id, data={}):
    if not id:
        return None

    url = "{}/{}".format(AUTHOR_URL, str(id))
    response = requests.put(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    if response.ok:
        return response
    else:
        return None


def put_book(id, data={}):
    if not id:
        return None

    url = "{}/{}".format(BOOK_URL, str(id))
    response = requests.put(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    if response.ok:
        return response
    else:
        return None


def delete_author(id):
    if not id:
        return None

    url = "{}/{}".format(AUTHOR_URL, str(id))
    response = requests.delete(url)
    if response.ok:
        return response
    else:
        return None


def delete_book(id):
    if not id:
        return None

    url = "{}/{}".format(BOOK_URL, str(id))
    response = requests.delete(url)
    if response.ok:
        return response
    else:
        return None