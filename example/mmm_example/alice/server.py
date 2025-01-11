import requests

from flask import Flask
from mmm_example.utils import http


class AliceServer(Flask):

    def __init__(self, alice_host, alice_port, bob_host, bob_port):
        super(AliceServer, self).__init__(__name__)

        self.alice_host = alice_host
        self.alice_port = alice_port
        self.bob_host = bob_host
        self.bob_port = bob_port

        self.add_url_rule('/hello', view_func=self.hello_request, methods=['POST'])

    def run_server(self):
        self.run(host=self.alice_host, port=self.alice_port)

    def hello_request(self):
        url = http(f'{self.bob_host}:{self.bob_port}/hello')
        bob_response = requests.post(url=url)
        return bob_response.text
