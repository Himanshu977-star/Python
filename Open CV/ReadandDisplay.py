import cv2

image=cv2.imread("Open CV/Image/image.jpg") #To read image

cv2.imshow("Elon Musk",image) #To show image
cv2.waitKey(0) #(0) means wait indefinitely until a key is pressed.
cv2.destroyAllWindows()