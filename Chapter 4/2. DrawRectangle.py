import cv2
import numpy as np

img=np.zeros((512,512,3))

#print(img)

#img[:]=255,0,0

cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)

cv2.imshow("Image",img)
cv2.waitKey(0)