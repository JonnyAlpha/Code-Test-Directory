# read and display an image file using OpenCV
import numpy as np
import cv2

image = cv2.imread("Dr1.jpg",0) #read the image
image = cv2.resize(image, (480, 640))
#uncomment and modify the following line if the image needs to be rotated
#image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("image", image)

cv2.waitKey(0)

cv2.destroyAllWindows()