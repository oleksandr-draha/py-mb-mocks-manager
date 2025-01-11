import os

import pytest

from requests import Session


ALICE_HOST = os.getenv('ALICE_HOST', '127.0.0.1')
ALICE_PORT = os.getenv('ALICE_PORT', '50517')


@pytest.mark.force_proxy
def test_hello(mocks_group):
    with mocks_group('hello'):
        response = Session().post(url=f'http://{ALICE_HOST}:{ALICE_PORT}/hello')
        assert response.text == 'world'
