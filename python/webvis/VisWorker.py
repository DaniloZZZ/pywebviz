import webbrowser
import json, time
import trio

from . import interface as ifc
from .helpers.threaded import threaded
from .helpers.AttrDict import AttrCbDict
from .websocket.ws_server import start_server as serve_ws
from .websocket.ws_server import stop as stop_ws
from .http_server import start_server as serve_http
from .http_server import stop as stop_http

COMMAND_GET_VAR="getvar"
COMMAND_GET_MPL="getmpl"

class Vis():
    def __init__(self, ws_port = 8000, vis_port=80, nb_name=None):
        self.ws_port = ws_port
        self.vis_port = vis_port
        self.vars = AttrCbDict(
            get_cb=lambda *x: None,
            set_cb=lambda *x: None
        )
        self.cached_vars = {}
        self.cached_msgs = {}
        self.active_vars = []
        self.nb_name = nb_name
        self.running = True

        args = ('localhost', ws_port, self._ws_handler, self._on_connect)
        self.pws = threaded( serve_ws, *args, name='ws')
        self.phttp = threaded( serve_http, vis_port, name='http')
        self.pmon = threaded( self._monitor_vars, name='monitor')

    def show(self):
        if self.nb_name:
            params = '?nb_name='+self.nb_name
        else: params = ''
        webbrowser.open_new_tab(
            f"localhost:{self.vis_port}/{params}"
        )

    def stop(self):
        print("Stopping websocket server")
        self.running = False
        stop_ws()
        #self.pws.terminate()
        #self.pws.join()

        print("Stopping Http server")
        stop_http()
        #self.phttp.terminate()
        #self.phttp.join()

    def _monitor_vars(self):
        async def monitor():
            while True:
                if not self.running: return
                time.sleep(1)
                print("Checking",self.active_vars)
                for varname in self.active_vars:
                    val = self.vars.get(varname)

                    cached_id = self.cached_vars.get(varname)
                    if cached_id==id(val): continue

                    msg = ifc.get_var( val, {'varname': varname} )
                    cached_msg = self.cached_msgs.get(varname)
                    if msg==cached_msg: continue

                    await self.ws.send_message(msg)
        trio.run(monitor)


    def _on_connect(self, ws):
        self.ws = ws

    async def _ws_handler(self, message_gen):
        async for message in message_gen:
            try:
                msg = json.loads(message)
            except json.JSONDecodeError:
                yield "Decode error" + str(message)
                continue
            command, params = msg.get('command'), msg.get('params')

            if command == 'get':
                # Check if the variable updated
                var = params.get('varname')
                if var:
                    val = self.vars.get(var)
                    cache = self.cached_vars.get(var)
                    if id(val) == cache: yield
                    self.cached_vars[var] = id(val)

                    try:
                        msg = ifc.get_var( val, params)
                        yield msg
                    except Exception as e:
                        msg = ifc.get_var(str(e), params)
                        yield msg
            if command=='setvars':
                self.active_vars = params

            yield "Unknown command"



