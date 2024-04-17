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
def BBBW1Event(RxData):
    socketio.emit('Web_BBBW1Event', RxData)
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
    app.run(host='192.168.0.233')
