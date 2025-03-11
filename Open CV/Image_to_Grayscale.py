import cv2

image=cv2.imread("Open CV/Image/image.jpg")

#Convert image to grayscale
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #cv2.cvtColor() converts images from one color space to another.
cv2.imshow("Grayscale",gray)
cv2.waitKey(0) 
cv2.destroyAllWindows()