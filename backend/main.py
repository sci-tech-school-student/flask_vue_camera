from flask import Flask, render_template, Response, redirect, url_for, request, jsonify, json
from camera import VideoCamera
from flask_cors import CORS, cross_origin
from dc_motor import Dc_motor, Motor_thread
import threading

# app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app = Flask(__name__)
CORS(app)

motor_thread = Motor_thread()

print('***** Starting route')


@app.route('/')
def index():
    return redirect(url_for('camera'))


@app.route('/get_request/', methods=['GET', 'POST'])
@app.route('/get_request/<key>', methods=['GET', 'POST'])
@cross_origin()
def get_request(key=None):
    data = request.method
    print('***** {} pushed'.format(key))
    if request.method == 'POST':
        dataDict = json.loads(request.data)
        print('***** {}'.format(dataDict))
        data = dataDict['text']
    motor_thread.key_watcher(key)
    return jsonify({'message': key})


@app.route('/camera', methods=['GET', 'POST'])
def camera():
    return render_template('index.html', request=request)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, threaded=True)
