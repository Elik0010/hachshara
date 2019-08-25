import numpy as np
import cv2

def LPF_filter(img, rad):
    length = rad * 2 + 1
    kernel = np.ones((length,length))
    rows, cols = img.shape
    res = np.zeros(img.shape)
    for i in range(rows - length):
        for j in range(cols - length):
            res[i + rad - 1,j + rad - 1] = np.mean(kernel *  img[i:i + length, j:j + length])
    return res.astype('uint8')

def HPF_filter(img, rad):
    length = rad * 2 + 1
    kernel = np.ones((length,length)) * -1
    mid = rad
    kernel[mid,mid] = length * length - 1
    rows, cols = img.shape
    res = np.zeros(img.shape)
    for i in range(rows - length):
        for j in range( cols - length):
            res[i + rad,j + rad] = np.mean(kernel * img[i:i + length, j:j + length])
    return res.astype('uint8')


def median_filter(img, rad):
    length = 2 * rad + 1
    rows, cols = img.shape
    res = np.zeros(img.shape)
    for i in range(rows - length):
        for j in range(cols - length):
            res[i + rad, j + rad] = np.median(img[i:i+length,j:j+length])
    return res.astype('uint8')












#TEST CODE
img = cv2.imread('room.jpg', cv2.IMREAD_GRAYSCALE)
rad = 3
img_LPF = LPF_filter(img, rad)
img_HPF = HPF_filter(img, rad)
img_med = median_filter(img, rad)
cv2.imshow("low pass filter", img_LPF)
cv2.imshow("high pass filter", img_HPF)
cv2.imshow("mixed", img_LPF + img_HPF)
cv2.imshow("median", img_med)
cv2.waitKey(0)
cv2.destroyAllWindows()