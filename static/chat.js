var socket = io.connect('http://localhost:5000');

function sendMessage() {
    var message = document.getElementById('messageInput').value;
    socket.emit('message_to_flask', message);
    document.getElementById('messages').innerText += message + '\n';
}

socket.on('js_event', function(data) {
    str = data.data;
    if(str === "ping\r\n")
        return;
    document.getElementById('messages').innerText += str;
});