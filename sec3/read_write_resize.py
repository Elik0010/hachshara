import cv2






img = cv2.imread("soldier.jpg")
img = cv2.resize(img, (250,250))
cv2.imwrite('smallSoldier.jpg', img)