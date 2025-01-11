import os

from mmm_example.alice.server import AliceServer
from mmm_example.bob.server import BobServer


ALICE_HOST = os.getenv('ALICE_HOST', '127.0.0.1')
ALICE_PORT = int(os.getenv('ALICE_PORT', '50517'))
BOB_HOST = os.getenv('BOB_HOST', '127.0.0.1')
BOB_PORT = int(os.getenv('BOB_PORT', '50518'))


def run_alice_server():
    alice = AliceServer(
        alice_host=ALICE_HOST,
        alice_port=ALICE_PORT,
        bob_host=BOB_HOST,
        bob_port=BOB_PORT,
    )
    alice.run_server()


def run_bob_server():
    bob = BobServer(
        bob_host=BOB_HOST,
        bob_port=BOB_PORT,
    )
    bob.run_server()
