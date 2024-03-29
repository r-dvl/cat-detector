from flask import Flask, render_template, Response
import cv2
from camera import motionCam

app = Flask(__name__)

def gen_frames():
    while True:
        success, frame = motionCam.readCap() # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def start():
    app.run(host="0.0.0.0", port=8888)

if __name__ == "__main__":
    start()