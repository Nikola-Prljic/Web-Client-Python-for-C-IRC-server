const socket = new WebSocket('ws://localhost:8765'); // Connect to the WebSocket server

function scrollTextboxToBottom() {
    var chatContainer = document.querySelector('.content');
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Send a message to the WebSocket server when a button is clicked

function sendMessage() {
    message = document.getElementById('messageInput').value;
    if (message === "")
        return;
    socket.send(message);
    /* document.getElementById('messages').style.textAlign = "left"; */
    var wrappedMessage = wrapLongMessage(message);
    document.getElementById('messages').innerHTML += '<span style="display: block; text-align: right; ">' + wrappedMessage + '</span>';
    scrollTextboxToBottom()
    messageInput.value = '';
}

document.getElementById('sendbutton').addEventListener('click', function() {
    sendMessage();
});

function enterKeyListener() {
    var input = document.getElementById("messageInput");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    })
};

socket.onmessage = function(event) {
    receivedMessage = event.data;
    document.getElementById('messages').innerHTML += '<span style="display: block; text-align: left;">' + receivedMessage + '</span>';
    scrollTextboxToBottom()
};

function wrapLongMessage(message) {
    var maxLength = 40; // Maximum characters per line
    var wrappedMessage = '';
    for (var i = 0; i < message.length; i += maxLength) {
        wrappedMessage += message.substring(i, i + maxLength) + '<br>';
    }
    return wrappedMessage;
}

enterKeyListener()