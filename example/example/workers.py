import os

from example.alice.server import AliceServer
from example.bob.server import BobServer

ALICE_HOST = os.getenv("ALICE_HOST")
ALICE_PORT = os.getenv("ALICE_PORT")
BOB_HOST = os.getenv("BOB_HOST")
BOB_PORT = os.getenv("BOB_PORT")


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
