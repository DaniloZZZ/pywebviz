from trio_websocket import ConnectionClosed

async def message_gen(ws):
    while True:
        try:
            msg = await ws.get_message()
            print("Got message: %s"% msg)
            yield msg
        except ConnectionClosed:
            print('ConnectionClosed while reading')
            return
