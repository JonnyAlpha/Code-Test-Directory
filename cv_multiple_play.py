import numpy as np
import keyboard
import cv2 as cv
from ffpyplayer.player import MediaPlayer

def play_video(file):
    cap = cv.VideoCapture(file)
    player = MediaPlayer(file)
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

def main():
    video1 = "video1.mp4"
    video2 = "video2.mp4"
    #play_video(video1)
    #current_video = video1
    while True:
        #play_video(video1)
        #current_video = video1
        try:
            if keyboard.is_pressed('c'):
                play_video(video1)
                current_video = video1
                if current_video == video1:
                    play_video(video2)
                    current_video = video2
                elif current_video == video2:
                    play_video(video1)
                    current_video = video1
        except:
            break
            
if __name__ == '__main__':
    main()
