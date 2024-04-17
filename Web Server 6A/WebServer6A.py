import socket
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import logging

app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'
socketio = SocketIO(app)
socket.getaddrinfo('localhost', 8080)


@app.route('/')
def index():
    logging.warning("See this message in Flask Debug Toolbar!")
    return render_template('index.html')


@socketio.event
def ControlUSR0Led(RxData):
    if RxData == 'on':
        socketio.emit('ControlUSR0Led', RxData)
    if RxData == 'off':
        socketio.emit('ControlUSR0Led', RxData)


@socketio.event
def BBBW1Event(RxData):
    socketio.emit('BBBW1Event', RxData)
    print('Receive Data from BBBW1')


@socketio.event
def BBBW2Event(RxData):
    socketio.emit('Web_BBBW2Event', RxData)
    print('Receive Data from BBBW2')


@socketio.event
def BBBW3Event(RxData):
    socketio.emit('Web_BBBW3Event', RxData)
    print('Receive Data from BBBW3')


@socketio.event
def BBBW4Event(RxData):
    socketio.emit('Web_BBBW4Event', RxData)
    print('Receive Data from BBBW4')


if __name__ == '__main__':
    app.run(host='192.168.0.113', port=8080, debug=True)
