import cv2

img=cv2.imread("Resources/baboon.png")

print(img.shape) 

imgResize= cv2.resize(img,(412,412))

print("Resize Image Shape",imgResize.shape)

cv2.imshow("Baboon",imgResize)

cv2.waitKey(0)