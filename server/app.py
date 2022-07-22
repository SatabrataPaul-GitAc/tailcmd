import socketio
import os
import subprocess
import eventlet
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sio = socketio.Server()

root_dir = "/home/ec2-user"
print(root_dir)

class Handler(FileSystemEventHandler):
    def __init__(self,num,file_path,sid):
        self.num = num
        self.file_path = file_path
        self.sid = sid

    def on_modified(self, event):
        run_cmd = subprocess.Popen("tail -{} {}".format(self.num, self.file_path), stdout=subprocess.PIPE, shell=True)
        file_data = run_cmd.communicate()[0].decode()
        print(file_data)
        sio.emit('file_data_modified', data={'content': file_data})


@sio.event
def connect(sid,environ,auth):
    print("Websocket Connection established")
    print("Session id: {}".format(sid))

@sio.on('fetch')
def fetch(sid, data):
    file = data.get('file', '')
    num = data.get('num')
    file_path = os.path.join(root_dir, file)
    if not os.path.exists(file_path):
        sio.emit('error', {'error': 'File not found on server'})
        return

    run_cmd = subprocess.Popen("tail -{} {}".format(num, file_path), stdout=subprocess.PIPE, shell=True)
    file_data = run_cmd.communicate()[0].decode()
    print(file_data)
    observer = Observer()
    monitor_event_handler = Handler(num,file_path,sid)
    observer.schedule(monitor_event_handler, file_path, recursive=True)
    observer.start()
    sio.emit('file_data', data={'content': file_data})

app = socketio.WSGIApp(sio)
eventlet.wsgi.server(eventlet.listen(('172.31.44.167', 8000)), app)
