import numpy as np
import matplotlib.pyplot as plt
import cv2


def active_contour(img):
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    img = cv2.Canny(img, 150, 200)
    cv2.imshow("img:",img)
    cv2.waitKey(0)


img = "soldier.jpg"
active_contour(img)