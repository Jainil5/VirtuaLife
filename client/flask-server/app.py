import cv2
from playsound import playsound
from flask import Flask, render_template, Response, send_from_directory
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from appf import *


app = Flask(__name__, static_url_path="",static_folder="../build")
camera = cv2.VideoCapture(0)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# FingerCounter, vRemote,  Blind: voice assisted Finger Counter, v va Remote


@app.route('/')
def index():
    return send_from_directory(app.static_folder,"index.html")

@app.route('/soon')
def soon():
    return render_template('soon.html')

@app.route('/vb')
def vb():
    return render_template('vb.html')

@app.route('/remote')
def remote():
    return render_template('remote.html')

@app.route('/vRemoteVA')
def vRemoteVA():
    return render_template('vRemoteVA.html')

@app.route('/counter')
def counter():
    return render_template('counter.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/rps')
def rps():
    return render_template('rps.html')

@app.route('/video_counter')
def video_counter():
    return Response(generate_frames_counter(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_VB')
def video_VB():
    return Response(generate_frames_VB(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_remote')
def video_remote():
    return Response(generate_frames_remote(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_vRemoteVA')
def video_vRemoteVA():
    return Response(generate_frames_vRemoteVA(), mimetype='multipart/x-mixed-replace; boundary=frame')    

@app.route('/video_quiz')
def video_quiz():
    return Response(generate_frames_quiz(), mimetype='multipart/x-mixed-replace; boundary=frame')

  

if __name__ == "__main__":
    app.run(debug=True)


# <video src='/videos/VL1.mp4' autoPlay loop muted />