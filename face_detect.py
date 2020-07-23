import cv2
import numpy as np


face_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
eye_glasses_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if(cap.isOpened == False):
    print("wrong path")
while(cap.isOpened()):

    ret, frame = cap.read()

    if(ret == True):
        faces = face_classifier.detectMultiScale(frame,2,5)
        eyes = eye_classifier.detectMultiScale(frame,2,5)   
        eyes_glasses = eye_glasses_classifier.detectMultiScale(frame,2,5)     

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)

        for (x,y,w,h) in eyes:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

        for (x,y,w,h) in eyes_glasses:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)


        cv2.imshow('Gray video',frame)
        if cv2.waitKey(30) & 0xFF == 27:
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()


