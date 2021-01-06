from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import mido
from mido import Message


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

outp = mido.open_output('IAC Driver Bus 1')


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('slider')
def on_slider(message):
    slider_val = message['data']
    print('got slider', slider_val)
    cc_val = int(127 * (slider_val / 100))
    cc = Message('control_change', channel=0, control=1, value=cc_val, time=0)
    outp.send(cc)


@socketio.on('connect')
def on_connect():
    print('Client connected')


@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
