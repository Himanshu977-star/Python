import cv2

image=cv2.imread("Open CV/Image/image.jpg")

resized=cv2.resize(image,(1000,800))
cv2.imshow("Resized Image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()