import cv2
#Load Haar Cascade Model
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)

if not cap.isOpened():
  print("Error:Could not open webcam")
  exit()

while True:
  ret,frame=cap.read()

  if not ret:
    print("Error: Could not read frame")
    break  
  #Converts the image to grayscale because Haar Cascade works better on grayscale images.
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  faces=face_cascade.detectMultiScale(gray,1.3,5) #Uses detectMultiScale() to detect faces.
  for (x,y,w,h) in faces:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

  cv2.imshow("Haar Cascade",frame)

  if cv2.waitKey(1) & 0xFF == ord('q'): 
    break

cap.release()
cv2.destroyAllWindows()  