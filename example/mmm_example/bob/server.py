from flask import Flask


class BobServer(Flask):

    def __init__(self, bob_host, bob_port):
        super(BobServer, self).__init__(__name__)
        self.bob_host = bob_host
        self.bob_port = bob_port

        self.add_url_rule('/hello', view_func=self.hello_request, methods=['POST'])

    def run_server(self):
        self.run(host=self.bob_host, port=self.bob_port)

    def hello_request(self):
        return 'world'
