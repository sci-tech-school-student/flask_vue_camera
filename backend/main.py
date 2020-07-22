from flask import Flask, render_template, Response, redirect, url_for, request, jsonify, json
from camera import VideoCamera
from flask_cors import CORS, cross_origin

# app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return redirect(url_for('camera'))


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/get_request', methods=['GET', 'POST'])
@cross_origin()
def get_request():
    data = request.method
    print('***** {} request is coming'.format(data))
    if request.method == 'POST':
        dataDict = json.loads(request.data)
        # print('***** {}'.format(dataDict))
        data = dataDict['text']

    return jsonify({'message': data})


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


@app.route('/get_key')
def get_key():
    data = {
        'request': 'request'
    }
    return Response(data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, threaded=True)
