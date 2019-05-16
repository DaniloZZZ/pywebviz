const addr = 'localhost:8000'

export function main(){
    ws = ws_connect(addr)
    ws.send("hello")
}

function ws_connect(addr){
    var ws = new WebSocket("ws://"+addr);
    return ws
}
