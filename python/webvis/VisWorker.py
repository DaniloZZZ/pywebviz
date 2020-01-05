import webbrowser
from hosta import Happ

from .helpers.threaded import threaded
from .helpers.AttrDict import AttrCbDict
from .http_server import create_server as create_http
from webvis.VisVars import VisVars

COMMAND_GET_VAR="getvar"
COMMAND_GET_MPL="getmpl"


class Vis():
    def __init__(self, ws_port = 7700, vis_port=7000, nb_name=None):
        self.ws_port = ws_port
        self.vis_port = vis_port
        self.vars = AttrCbDict(
            get_cb=lambda *x: None,
            set_cb=lambda *x: None
        )
        self.active_vars = []
        self.nb_name = nb_name

        self.app = Happ(addr='localhost', port=ws_port)
        self.app.vars = VisVars()
        self.app._on_val_set(None, self.app.vars)

        self.http_server = create_http(port=vis_port)

        self.vars = self.app.vars

    def start(self):
        self.app.run()
        self.phttp = threaded( self.http_server.serve_forever, name='http')

    def show(self):
        if self.nb_name:
            params = '?p='+self.nb_name
        else: params = ''
        webbrowser.open_new_tab(
            f"localhost:{self.vis_port}/{params}"
        )

    def stop(self):
        print("Stopping websocket server")
        self.app.stop()
        print("Stopping app server")
        self.http_server.shutdown()

    def _on_connect(self, ws):
        self.ws = ws
