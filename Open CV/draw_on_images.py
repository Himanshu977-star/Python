import cv2

image=cv2.imread("Open CV/Image/image.jpg")

cv2.rectangle(image,(50,50),(200,200),(0,255,0),3)
cv2.circle(image,(150,150),50,(255,0,0),-1)
cv2.imshow("Elon Musk",image) #To show image
cv2.waitKey(0) #(0) means wait indefinitely until a key is pressed.
cv2.destroyAllWindows()