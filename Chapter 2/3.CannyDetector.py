import cv2

img=cv2.imread("Resources/lenna.png")

imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgCanny= cv2.Canny(img,150,200) 

cv2.imshow("Image Canny",imgCanny)
cv2.waitKey(0)