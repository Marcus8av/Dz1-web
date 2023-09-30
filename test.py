import pytest

from Rest_api import get



def test_1(get_token):
    result = get(get_token)
    lst = result['data']
    lst_id = [el['id'] for el in lst]
    assert 80532 in lst_id


def test_2(create_post):
    assert create_post['title'] == 'Test Post'
    assert create_post['description'] == 'This is a test post'
    assert create_post['content'] == 'Test post content'

if __name__ == '__main__':
    pytest.main(['-v'])