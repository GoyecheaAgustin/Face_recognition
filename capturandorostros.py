import cv2
import os
import imutils

personName="Agustin"
dataPatch = ('D:/Users/Agustin Goyechea/Desktop/Ingenieria/5to/PDS/recoface/data100')
personaPatch = dataPatch + '/' + personName

if not os.path.exists(personaPatch):
    print('Carpeta creada: ', personaPatch)
    os.makedirs(personaPatch)

cap = cv2.VideoCapture('Moya.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
    ret, frame = cap.read()
    if ret == False: break
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,+h),(0,255,0),2)
        rostro = auxFrame[y:y+h,x:x+w]    
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(personaPatch + '/rostro{}.jpg'.format(count),rostro)
        count+=1
    k = cv2.waitKey(1)
    if k == 27 or count==100:
        print("Termino la captura de rostros")
        break

cap.release()
cv2.destroyAllWindows