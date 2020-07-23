import face_recognition
import os
import cv2


KNOWN_FACES_DIR = "known_faces"
TOLERANCE = 0.5
MODEL = "hog"

known_faces = []
known_names = []

for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        face_encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(face_encoding)
        known_names.append(name)

cap = cv2.VideoCapture(0)

print(known_names)
while(cap.isOpened()):

    ret, image = cap.read()

    if(ret == True):
        locations = face_recognition.face_locations(image, model=MODEL)
        encodings = face_recognition.face_encodings(image,locations)
        
        for face_encoding, face_location in zip(encodings,locations):
            results = face_recognition.compare_faces(known_faces,face_encoding, TOLERANCE)
            match = None

            if(any(results) == True):
                match = known_names[results.index(True)]

                print(f'match found: {match}')

                top_left = (face_location[3], face_location[0])
                bottom_rigth = (face_location[1], face_location[2])

                cv2.rectangle(image,top_left,bottom_rigth,(0,0,255),5)

                top_left = (face_location[3], face_location[2])
                bottom_rigth = (face_location[1], face_location[2]+22)

                cv2.rectangle(image,top_left,bottom_rigth,(0,0,255),cv2.FILLED)
                cv2.putText(image,match,(face_location[3]+10, face_location[2]+15),cv2.FONT_HERSHEY_PLAIN, 1,(255,255,255),5)

    else:
        break

    cv2.imshow('video',image)
    if(cv2.waitKey(30) & 0xFF == 27):
        break

cap.release()
cv2.destroyAllWindows()


        
