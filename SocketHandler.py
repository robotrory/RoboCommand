import pyaudio
from tornado import websocket

clients = []
stream = None

p = pyaudio.PyAudio()

class SocketHandler(websocket.WebSocketHandler):
  def check_origin(self, origin):
    return True

  def open(self):
    global stream
    if len(clients) < 1:
      print("opening stream")
      stream = p.open(format=p.get_format_from_width(2),
                      channels=1,
                      rate=16000,
                      output=True)

    if self not in clients:
      clients.append(self)

  def on_close(self):
    global stream
    if self in clients:
      clients.remove(self)

    if len(clients) < 1:
      print("closing stream")
      stream.stop_stream()
      stream.close()
      stream = None

  def on_message(self, message):
    global stream

    if stream is not None:
      print("message")
      stream.write(message)
