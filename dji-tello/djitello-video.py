import time, cv2
from threading import Thread
from djitellopy import Tello
import requests
import json

URL = 'http://127.0.0.1:8000/predictimage'

tello = Tello()

tello.connect()
tello.streamon()

frame_read = tello.get_frame_read()

height, width, _ = frame_read.frame.shape
cv2.imwrite("picture.png", frame_read.frame)

while True: 
    img = frame_read.frame
    img = cv2.resize(img, (360, 240))

    cv2.imwrite("picture.png", frame_read.frame)
    file = {'file': open('./picture.png', 'rb')}

    response = requests.post(url=URL, files=file) 
    json_resp = json.loads(response.text)
    cv2.putText(img, f"{json_resp['class_name']}: {json_resp['confidence']}", (150, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, 2)

    cv2.imshow("DJI Tello", img)
    cv2.waitKey(1)


