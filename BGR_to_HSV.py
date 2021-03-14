import cv2
import numpy as np

bgr_red = np.uint8([[[0, 0, 255]]])
hsv_red = cv2.cvtColor(bgr_red, cv2.COLOR_BGR2HSV)
print(hsv_red)
hsv =hsv_red.reshape(3)
print(hsv)