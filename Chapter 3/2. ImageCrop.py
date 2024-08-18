import cv2

img=cv2.imread("Resources/baboon.png")

print(img.shape) 

imgCropped = img[0:200,200:500]


cv2.imshow("Cropped Baboon",imgCropped)

cv2.waitKey(0)