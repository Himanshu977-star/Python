import cv2

cap=cv2.VideoCapture(0) #to capture video 0:default webcam 1:external webcam 

if not cap.isOpened():
  print("Error:Could not open webcam")
  exit()

while True:
  ret,frame=cap.read()
  #ret is a boolean variable that returns true if the frame is available
  #frame is an array representing the image
  if not ret:
    print("Error: Could not read frame")
    break  

  cv2.imshow("Webcam Video", frame)

  if cv2.waitKey(1) & 0xFF == ord('q'): 
    break

cap.release()
cv2.destroyAllWindows()  