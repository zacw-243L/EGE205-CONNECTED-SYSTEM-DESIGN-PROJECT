from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask_socketio import emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.event
def ControlUSR0Led(RxData):
    if RxData == 'on':
        socketio.emit('ControlUSR0Led', RxData)
    if RxData == 'off':
        socketio.emit('ControlUSR0Led', RxData)


@socketio.event
def BBBWEvent(RxData):
    socketio.emit('Web_BBBWEvent', RxData)
    print('Receive Data from BBBW')


if __name__ == '__main__':
    app.run(host='192.168.0.233')
