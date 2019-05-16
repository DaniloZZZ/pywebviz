
const addr = 'localhost:8000'
function get_xpath(path){
    nodes = document.evaluate(path,
        document, null, XPathResult.ANY_TYPE, null); 
    return nodes.iterateNext()
}

function main(){
    var ws = new WebSocket("ws://"+addr);
    ws.onopen = function(){
        console.info('connected');
        ws.send("hello");
        start_polling(ws);
    }
    ws.onerror = e=>{
        console.err(e);
    }
    ws.onmessage = m=>{
        console.log('got ws:',m.data);
    }

    container = document.getElementById("variable")

}
function start_polling(ws){

    value_node = get_xpath('//div[@id="variable"]/label')
    key_node = get_xpath('//div[@id="variable"]/input')
    step = function(){

        key = key_node.value
        //console.log('getting key',key)


        ws.send(
            'getvar:'+key
        )
    }
    ws.onmessage = m=>{
        console.log('got ws:',m.data);
        value_node.innerHTML = m.data
    }

    setInterval(step, 200);
}
