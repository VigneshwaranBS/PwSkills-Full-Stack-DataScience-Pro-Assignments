from flask import Flask, render_template
from flask_socketio import SocketIO
import time
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secret key

socketio = SocketIO(app, cors_allowed_origins="*")

def time_updater():
    while True:
        current_time = time.ctime()
        socketio.emit('update_time', current_time)
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    current_time = time.ctime()
    socketio.emit('update_time', current_time)

if __name__ == '__main__':
    updater_thread = Thread(target=time_updater)
    updater_thread.daemon = True
    updater_thread.start()
    socketio.run(app, debug=True)
