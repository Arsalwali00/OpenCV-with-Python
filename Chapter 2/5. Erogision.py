import cv2
import numpy as np

img=cv2.imread("Resources/lenna.png")

kernal=np.ones((5,5),np.uint8)

imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny= cv2.Canny(img,150,200) 

imgDialation= cv2.dilate(imgCanny,kernal,iterations=1)

imgEroded= cv2.erode(imgDialation,kernal,iterations=1)

cv2.imshow("Erodid Image",imgEroded)

cv2.waitKey(0)