from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import socket, threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080       # The port used by the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message_to_flask')
def handle_message(message):
    print('Received message from HTML:', message)
    send_message_to_tcp_server(message)

def send_message_to_tcp_server(message):
    message += "\n"
    try:
        sock.sendall(message.encode())
    except socket.error as e:
        print("Socket error:", e)

def handelData(data):
    str = data.decode()
    str = str.split(":")
    print(str)
    if len(str) == 2:
        return str[1]
    return str[2]

@socketio.on('trigger_event')
def recvMsg():
    while True:
        data = sock.recv(1024)
        if len(data) == 0:
            return
        print("recev from irc: ", data.decode(), end="")
        str = handelData(data)
        socketio.emit('js_event', {'data': str})

if __name__ == '__main__':
    sock.connect((HOST, PORT))
    t = threading.Thread(target=recvMsg)
    t.daemon = True
    t.start()
    socketio.run(app)
    sock.close()