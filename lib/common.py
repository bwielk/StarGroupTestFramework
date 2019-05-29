import requests


def basic_get_request(url):
    session = requests.Session()
    response = session.get(url)
    session.close()
    return response


def basic_post_request(url, json_body):
    session = requests.Session()
    response = session.post(url, json=json_body)
    session.close()
    return response


def basic_delete_request(url):
    session = requests.Session()
    response = session.delete(url)
    session.close()
    return response
