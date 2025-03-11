import cv2

image=cv2.imread("Open CV/Image/image.jpg")
#to show the edges of the image
edges=cv2.Canny(image,100,200)
cv2.imshow("Edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()