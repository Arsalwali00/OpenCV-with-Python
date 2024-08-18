import cv2
import numpy as np

img=np.zeros((512,512,3))

#print(img)

#img[:]=255,0,0

cv2.circle(img,(400,50),30,(255,255,0),5)

cv2.imshow("Image",img)
cv2.waitKey(0)