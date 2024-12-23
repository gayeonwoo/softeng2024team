from flask import Flask, Response
from picamera import PiCamera
from time import sleep
import io

app = Flask(__name__)
camera = PiCamera()

def generate_frames():
    stream = io.BytesIO()
    for _ in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
        stream.seek(0)
        frame = stream.read()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        stream.seek(0)
        stream.truncate()

@app.route('/monitor')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    camera.resolution = (640, 480)
    camera.framerate = 24
    sleep(2)  # 카메라 초기화 시간
    app.run(host='0.0.0.0', port=5000)
