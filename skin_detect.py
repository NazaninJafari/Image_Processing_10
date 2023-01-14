import cv2
import numpy as np

camera = cv2.VideoCapture(0)

#width  = int(camera.get(3))
#height = int(camera.get(4))
lower = np.array([0 ,48 , 80], dtype='uint8')
upper = np.array([20, 255, 255], dtype='uint8')

while True:
    ret, frame = camera.read()
    hsv_converted = cv2.cvtColor(frame ,cv2.COLOR_BGR2HSV)
    
    if not ret:
        break

    skin_mask = cv2.inRange(hsv_converted, lower, upper) 
    skin = cv2.bitwise_and(frame, frame, mask=skin_mask)

    key = cv2.waitKey(1)
    if key == 27: #Esc
        break

    cv2.imshow('skin_detection', skin)

camera.release()
#cv2.destroyAllWindows()