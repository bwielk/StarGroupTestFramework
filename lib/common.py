import requests


def basic_get_request(url):
    session = requests.Session()
    response = session.get(url)
    return response


def basic_post_request(url, json_body):
    session = requests.Session()
    response = session.post(url, json=json_body)
    return response

