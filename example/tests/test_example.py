import os

from requests import Session

from mountebank_mocks_manager.demo import world

ALICE_HOST = os.getenv("ALICE_HOST", "127.0.0.1")
ALICE_PORT = os.getenv("ALICE_PORT", "50517")


def test_hello():
    response = Session().post(url=f"http://{ALICE_HOST}:{ALICE_PORT}/hello")
    assert response.text == world()
