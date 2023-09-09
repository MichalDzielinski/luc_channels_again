console.log('hello hello')

const socket = new WebSocket('ws://'+window.location.host + '/ws/test_statistic/');
console.log(socket)

socket.onmessage = function(e){
    console.log('Server:'+ e.data);
}

socket.onopen = function(e){
    socket.send(JSON.stringify({
        'message': 'Hello from the client',
        'sender': 'test sender',
    }))
}

