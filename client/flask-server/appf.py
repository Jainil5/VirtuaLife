import os
import time
import cv2
from playsound import playsound
from cvzone.HandTrackingModule import HandDetector
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
import webbrowser
import requests

camera = cv2.VideoCapture(0)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))



def getCount(ar):
    if ar == [0, 0, 0, 0, 0]:
        return 0
    elif ar == [0, 1, 0, 0, 0]:
        return 1
    elif ar == [0, 1, 1, 0, 0]:
        return 2
    elif ar == [0, 1, 1, 1, 0]:
        return 3
    elif ar == [0, 1, 1, 1, 1]:
        return 4
    elif ar == [1, 1, 1, 1, 1]:
        return 5
    elif ar == [1, 1, 0, 0, 0]:
        return 6
    elif ar == [1, 1, 1, 0, 0]:
        return 7
    elif ar == [1, 1, 1, 1, 0]:
        return 8
    elif ar == [0, 1, 0, 0, 1]:
        return 9
    elif ar == [1, 1, 0, 0, 1]:
        return 10

def getSound(n):
    if n == 0:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S0.mp3')
    elif n == 1:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S1.mp3')
    elif n == 2:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S2.mp3')
    elif n == 3:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S3.mp3')
    elif n == 4:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S4.mp3')
    elif n == 5:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S5.mp3')
    elif n == 6:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S6.mp3')
    elif n == 7:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S7.mp3')
    elif n == 8:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S8.mp3')
    elif n == 9:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S9.mp3')
    elif n == 10:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S10.mp3')
    else:
        print("Not valid gesture")

def playVideo(n: int):
    try:
        if n == 0:
            pass
        elif n == 1:
            item = "Until I found You"
            return "https://music.youtube.com/watch?v=oIKuyj2GQtY&list=OLAK5uy_l9YOtSVbG-PNcH_34SJ6x6JD-us_OwWMA"
        elif n == 2:
            # Often Kygo Remix
            return "https://music.youtube.com/watch?v=qsDfFE2i0Ws&list=OLAK5uy_ly01GlEiOSaOGY96EerK02RdL2RS5vNMA"
        elif n == 3:
            # Playlist vibe
            return "https://music.youtube.com/watch?v=aSeKe_9qgqU&list=PLEZtw9WFgxhuQtHuCg38QcW89aN6pFwfQ"
        elif n == 4:
            # YT playlist 1
            return "https://music.youtube.com/watch?v=AJL_aVxqMEc&list=PLEZtw9WFgxhtTxc69kE2SGay-ixhRsrFv"
        elif n == 5:
            # YT playlist 2
            return "https://music.youtube.com/watch?v=TA1W-pHNKl8&list=PLEZtw9WFgxhvRWyo3Soz_rwJv8A9QvzNj"
    except:
        print("Error")
"""
def generate_frames():
    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:

            img, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
"""


def generate_frames_counter():
    while True:
            ## read the camera frame
            success, frame = camera.read()
            if not success:
                break
            else:
                detector = HandDetector(detectionCon=0.8, maxHands=2)
                success, img = camera.read()
                hands, img = detector.findHands(img)
                if hands:
                    if len(hands) == 1:
                        hand1 = hands[0]
                        h1f = detector.fingersUp(hand1)
                        h1c = getCount(h1f)
                        if h1c is not None:
                            getSound(h1c)
                    if len(hands) == 2:
                        hand1 = hands[0]
                        h1f = detector.fingersUp(hand1)
                        h1c = getCount(h1f)
                        hand2 = hands[1]
                        h2f = detector.fingersUp(hand2)
                        h2c = getCount(h2f)
                        listT = [11, 12, 13]
                        if h1c is not None and h2c is not None:
                            if h1c == 5 or h2c == 5:
                                total = h1c + h2c
                                if h1c == 5 or h2c == 5:
                                    getSound(total)
                                if h1c == 0 or h2c == 0:
                                    getSound(total)
            # SAME
            img, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def generate_frames_VB():
    while True:
        ## read the camera frame
            success, frame = camera.read()
            if not success:
                break
            else:
                detector = HandDetector(detectionCon=0.9, maxHands=2)
                success, img = camera.read()
                hands, img = detector.findHands(img)
                if hands:
                    if len(hands) == 2:
                        hand1 = hands[0]
                        handType1 = hand1["type"]
                        h1f = detector.fingersUp(hand1)
                        h1c = getCount(h1f)
                        hand2 = hands[1]
                        handType2 = hand2["type"]
                        h2f = detector.fingersUp(hand2)
                        h2c = getCount(h2f)
                        listV1 = [-65.25, -23.654823303222656, -10.329694747924805, -5.290315628051758,
                                  -3.4243249893188477, 0, 0]
                        listB1 = [0, 20, 40, 60, 80, 100, 100]
                        vs = 2  # volume
                        bs = 1  # Brightness
                        # Volume and Brightness
                        if handType1 == "Left":  # Left Host
                            if h1c == vs:
                                fc = h2c
                                for i in range(0, 6):
                                    if i == fc:
                                        vol = listV1[i]
                                        volume.SetMasterVolumeLevel(vol, None)
                            if h1c == bs:
                                fc = h2c
                                for i in range(0, 6):
                                    if i == fc:
                                        bri = listB1[i]
                                        sbc.set_brightness(bri)
                        if handType2 == "Left":  # Left Host
                            if h2c == vs:
                                fc = h1c
                                for i in range(0, 6):
                                    if i == fc:
                                        vol = listV1[i]
                                        volume.SetMasterVolumeLevel(vol, None)
                            if h2c == bs:
                                fc = h1c
                                for i in range(0, 6):
                                    if i == fc:
                                        bri = listB1[i]
                                        sbc.set_brightness(bri)
            

                img, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def generate_frames_remote():
    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            detector = HandDetector(detectionCon=0.8, maxHands=2)
            success, img = camera.read()
            hands, img = detector.findHands(img)
            if hands:
                if len(hands) == 2:
                    hand1 = hands[0]
                    handType1 = hand1["type"]
                    h1f = detector.fingersUp(hand1)
                    h1c = getCount(h1f)
                    cv2.putText(img, str(h1c), (10, 40), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
                    hand2 = hands[1]
                    handType2 = hand2["type"]
                    h2f = detector.fingersUp(hand2)
                    h2c = getCount(h2f)
                    cv2.putText(img, str(h2c), (400, 40), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
                    listV1 = [-65.25, -23.654823303222656, -10.329694747924805, -5.290315628051758, -3.4243249893188477, 0, 0]
                    listB1 = [0, 20, 40, 60, 80, 100, 100]
                    listU = []
                    vs = 2  # volume
                    ms = 3  # Music
                    bs = 1  # brightness
                    if handType1 == "Left":  # Left Host
                        # Volume
                        if h1c == vs:
                            fc = h2c
                            for i in range(0, 6):
                                if i == fc:
                                    vol = listV1[i]
                                    volume.SetMasterVolumeLevel(vol, None)
                        # Brightness
                        if h1c == bs:
                            fc = h2c
                            for i in range(0, 6):
                                if i == fc:
                                    bri = listB1[i]
                                    sbc.set_brightness(bri)
                        # Music
                        if h1c == ms:
                            fc = h2c
                            for i in range(1, 6):
                                if i == fc:
                                    url = playVideo(i)
                                    webbrowser.open_new(url)
                                    if url:
                                        listU.append(url)
                                    time.sleep(5)
                            if h2c == 0:
                                os.system("taskkill /im chrome.exe /f")
                                os.system("taskkill /im brave.exe /f")
                                os.system("taskkill /im msedge.exe /f")
                    if handType2 == "Left":  # Left Host
                        # volume
                        if h2c == vs:
                            fc = h1c
                            for i in range(0, 6):
                                if i == fc:
                                    vol = listV1[i]
                                    volume.SetMasterVolumeLevel(vol, None)
                        # Brightness
                        if h2c == bs:
                            fc = h1c
                            for i in range(0, 6):
                                if i == fc:
                                    bri = listB1[i]
                                    sbc.set_brightness(bri)
                        # Music
                        if h2c == ms:
                            fc = h1c
                            for i in range(1, 6):
                                if i == fc:
                                    url = playVideo(i)
                                    webbrowser.open_new(url)
                                    if url:
                                        listU.append(url)
                                    time.sleep(5)
                            if h1c == 0:
                                os.system("taskkill /im chrome.exe /f")
                                os.system("taskkill /im brave.exe /f")
                                os.system("taskkill /im msedge.exe /f")


            img, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def generate_frames_vRemoteVA():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            detector = HandDetector(detectionCon=0.8, maxHands=2)
            success, img = camera.read()
            hands, img = detector.findHands(img)
            if hands:
                if len(hands) == 2:
                    hand1 = hands[0]
                    lmList1 = hand1["lmList"]
                    handType1 = hand1["type"]
                    h1f = detector.fingersUp(hand1)
                    h1c = getCount(h1f)
                    hand2 = hands[1]
                    lmList2 = hand2["lmList"]
                    handType2 = hand2["type"]
                    h2f = detector.fingersUp(hand2)
                    h2c = getCount(h2f)
                    listV1 = [-65.25, -23.654823303222656, -10.329694747924805, -5.290315628051758, -3.4243249893188477, 0, 0]
                    listB1 = [0, 20, 40, 60, 80, 100, 100]
                    listU = []
                    vs = 2  # volume
                    ms = 3  # Music
                    bs = 1  # brightness
                    if handType1 == "Left":  # Left Host
                        # Volume
                        if h1c == vs:
                            fc = h2c
                            for i in range(0, 6):
                                if i == fc:
                                    vol = listV1[i]
                                    volume.SetMasterVolumeLevel(vol, None)
                        # Brightness
                        if h1c == bs:
                            fc = h2c
                            for i in range(0, 6):
                                if i == fc:
                                    bri = listB1[i]
                                    sbc.set_brightness(bri)
                        # Music
                        if h1c == ms:
                            fc = h2c
                            for i in range(1, 6):
                                if i == fc:
                                    url = playVideo(i)
                                    webbrowser.open_new(url)
                                    if url:
                                        listU.append(url)
                                    time.sleep(5)
                            if h2c == 0:
                                os.system("taskkill /im chrome.exe /f")
                                os.system("taskkill /im brave.exe /f")
                                os.system("taskkill /im msedge.exe /f")
                    if handType2 == "Left":  # Left Host
                        # volume
                        if h2c == vs:
                            fc = h1c
                            for i in range(0, 6):
                                if i == fc:
                                    vol = listV1[i]
                                    volume.SetMasterVolumeLevel(vol, None)
                        # Brightness
                        if h2c == bs:
                            fc = h1c
                            for i in range(0, 6):
                                if i == fc:
                                    bri = listB1[i]
                                    sbc.set_brightness(bri)
                        # Music
                        if h2c == ms:
                            fc = h1c
                            for i in range(1, 6):
                                if i == fc:
                                    url = playVideo(i)
                                    webbrowser.open_new(url)
                                    if url:
                                        listU.append(url)
                                    time.sleep(5)
                            if h1c == 0:
                                os.system("taskkill /im chrome.exe /f")
                                os.system("taskkill /im brave.exe /f")
                                os.system("taskkill /im msedge.exe /f")

            img, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



def generate_frames_quiz():
    url = 'http://127.0.0.1:1880/test-input'
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            detector = HandDetector(detectionCon=0.8, maxHands=2)
            success, img = camera.read()
            hands, img = detector.findHands(img)
            if hands:
                myobj = {'hand': 'yes'}
                requests.post(url, json = myobj)
            img, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
