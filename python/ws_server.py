import trio
from trio_websocket import serve_websocket, ConnectionClosed

def _print(*args):
    print("WebSocket::\t",*args)


async def ws_serve(addr,port, handler_func):
    async def server(request):
        ws = await request.accept()
        while True:
            try:
                message = await ws.get_message()
                #_print("got message",message)

                if not handler_func:
                    await ws.send_message(message)
                else:
                    resp = handler_func(message)
                    resp = str(resp)
                    await ws.send_message(resp)
            except ConnectionClosed:
                break
    await serve_websocket(server, addr, port, ssl_context=None)

def start_server(addr, port, handler_func=None):
    print(f"Starting ws server at {addr}:{port}")
    trio.run(ws_serve, addr, port, handler_func)

def main():
    start_server('127.0.0.1',8000)

if __name__=='__main__':
    main()



