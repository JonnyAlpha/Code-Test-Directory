import numpy as np
import cv2

image = cv2.imread("reference.jpg",0)

cv2.imshow("image", image)

cv2.waitKey(0)

cv2.destroyAllWindows()