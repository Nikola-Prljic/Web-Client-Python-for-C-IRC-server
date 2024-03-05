var socket = io.connect('http://localhost:5000');

function scrollTextboxToBottom() {
    var chatContainer = document.querySelector('.content');
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function sendMessage() {
    var message = document.getElementById('messageInput').value;
    if (message === "")
        return
    socket.emit('message_to_flask', message);
    document.getElementById('messages').innerText += message + '\n';
    scrollTextboxToBottom()
    messageInput.value = '';
}

function enterKeyListener() {
    var input = document.getElementById("messageInput");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    })
};

socket.on('js_event', function(data) {
    str = data.data;
    if(str === "ping\r\n")
        return;
    document.getElementById('messages').innerText += str;
    scrollTextboxToBottom()
});

enterKeyListener();