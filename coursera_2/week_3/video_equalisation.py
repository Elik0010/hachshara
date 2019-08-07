import cv2
import numpy as np




def video_equalize(vid_file):
    video = cv2.VideoCapture(vid_file)

    while video.isOpened():
        try:
            ret, frame1 = video.read()
            ret, frame2 = video.read()
            ret, frame3 = video.read()
        
            gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
            gray3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
        except:
            video = cv2.VideoCapture(vid_file)
            continue
        
        equ1 = cv2.equalizeHist(np.concatenate((gray1, gray2,gray3), axis=0))
        equ2 = cv2.equalizeHist(gray1)
        cv2.imshow('color', frame1)
        cv2.imshow('multiframe', equ1)
        cv2.imshow('singleframe', equ2)

        if cv2.waitKey(60) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


#TEST CODE
vid_file = 'video.mp4'
video_equalize(vid_file)