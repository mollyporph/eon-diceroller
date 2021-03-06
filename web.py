from flask import Flask , request, send_from_directory, jsonify
from werkzeug.routing import BaseConverter
import re
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import eventlet
import diceroller
app = Flask(__name__,static_url_path='')
socketio = SocketIO(app)
class Object(object):
    pass
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter

@app.route('/')
def root():
    return app.send_static_file('eon.html');

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)

@socketio.on('dicerollrequest')
def handle_diceroll(json):
    if re.match(r"(?:ob)?\d{1,2}t\d{1,3}(?:\+\d{1,2})?", json['roll']) is not None:
        (diceresult,ob,modifier) = diceroller.roll_dices(json['roll'])
        response = {"username": json['username'],"dices": diceresult,"obcount":ob,"dicesum": sum(diceresult)+modifier,"modifier": modifier}
        emit("dicerollresponse",response,room=json['room'])

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js',path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css',path)

if __name__ == '__main__':
    socketio.run(app)
