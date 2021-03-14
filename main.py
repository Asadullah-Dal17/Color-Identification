import cv2 as cv 
import numpy as np 

# Color detection function

def ColorDetection(image, LowerHSV , UpperHSV):
    
    hsvColorSpace = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    mask  = cv.inRange(hsvColorSpace, LowerHSV, UpperHSV)
    
    whitePixel = np.sum(mask==255)
    
    


# camera id 
camID =1
# Creating Camera object 
cap = cv.VideoCapture(camID)

# infinte loop, frame runing in the loop
while True:
    # reading frame from camera object 
    ret, frame = cap.read()

    # show the frame on the Screen 
    cv.imshow("frame ", frame)

    # define the Key, which will allow, the control over the loop, 
    # and allow other input operation, Like exit the loop,save the frame etc.
    Key = cv.waitKey(1)

    # breaking the loop here
    if Key ==ord("q"):
        break

# closing All windows which we have create using opencv 
cv.destroyAllWindows()
# releasing the camera/ closing the camera which we have openend.
cap.release()