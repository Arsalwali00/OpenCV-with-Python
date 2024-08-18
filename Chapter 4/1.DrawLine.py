import cv2
import numpy as np

img=np.zeros((512,512,3))

#print(img)

#img[:]=255,0,0

# cv2.line(img,(0,0),(300,300),(0,255,0),3) #creat a green line depend on values

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

cv2.imshow("Image",img)
cv2.waitKey(0)