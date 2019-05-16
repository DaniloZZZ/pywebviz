import webbrowser

from helpers import threaded
from ws_server import start_server as serve_ws
from http_server import start_server as serve_http

COMMAND_GET_VAR="getvar"

class Vis():
    def __init__(self, ws_port = 8000, vis_port=80):
        self.ws_port = ws_port
        self.vis_port = vis_port
        self.pws = threaded(
            serve_ws,
            'localhost', ws_port, self.handler
        )
        self.phttp = threaded(
            serve_http,
            vis_port
        )
        self.vars = {}

    def show(self):
        webbrowser.open(
            f"localhost:{self.vis_port}"
        )

    def stop(self):
        print("Stopping websocket server")
        self.pws.terminate()
        self.pws.join()

        print("Stopping Http server")
        self.phttp.terminate()
        self.phttp.join()


    def handler(self, message):
        try:
            command, args = message.split(":")
        except ValueError as e:
            return "Wrong format"

        if command==COMMAND_GET_VAR:
            return self.vars.get(args)

        return "Unknown command"



