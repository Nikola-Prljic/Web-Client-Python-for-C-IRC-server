const socket = new WebSocket('ws://localhost:8765');

socket.addEventListener('open', function (event) {
    console.log('WebSocket connection established.');
});

socket.addEventListener('message', function (event) {
    console.log('Received message:', event.data);
    const li = document.createElement('li');
    li.textContent = event.data;
    document.getElementById('messages').appendChild(li);
});

function sendMessage() {
    const message = document.getElementById('messageInput').value;
    socket.send(message);
    document.getElementById('messageInput').value = '';
}