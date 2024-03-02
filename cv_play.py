import numpy as np
import cv2 as cv
from ffpyplayer.player import MediaPlayer

video1 = 'video1.mp4'

cap = cv.VideoCapture(video1)
player = MediaPlayer(video1)
while cap.isOpened():
    ret, frame = cap.read()
    audio_frame, val = player.get_frame()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('frame', frame)
    if cv.waitKey(30) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
