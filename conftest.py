import pytest
import yaml
import requests
from Rest_api import get

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)


@pytest.fixture()
def get_token():
    response = requests.post(url=conf['url_login'], data={'username': conf['username'], 'password': conf['password']})
    return response.json()['token']

@pytest.fixture()
def create_post(get_token):
    headers = {'X-Auth-Token': get_token}
    data = {'title': 'Test Post', 'description': 'This is a test post', 'content': 'Test post content'}
    response = requests.post(url=conf['url_post'], headers=headers, data=data)
    assert response.status_code == 200
    yield response.json()
    requests.delete(url=f"{conf['url_post']}/{response.json()['id']}", headers=headers)



