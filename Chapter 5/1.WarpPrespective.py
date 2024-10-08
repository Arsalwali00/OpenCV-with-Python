import cv2
import numpy as np

img=cv2.imread("Resources/cards.jpg")

width,height= 250,350

pst1=np.float32([[111,219],[287,188],[154,482],[351,440]])
pst2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pst1,pst2)

imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)