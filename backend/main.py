from flask import Flask, render_template, Response, redirect, url_for
from camera import VideoCamera

# app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('camera'))


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/camera')
def camera():
    return render_template('index.html')


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
    # app.run(host='127.0.0.1', debug=True)
    app.run()
