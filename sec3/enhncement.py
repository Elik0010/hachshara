import numpy as np
import cv2


def negation(img):
    return 255 - img

def thresholding(img, thresh):
    return np.where(img >= thresh, 255, 0)


def contrast_stretching(img):
    prob = np.bincount(img.flatten())
    SHADES = 256
    img = img.astype('float32')
    res =  (img - np.min(img)) * (255 / (np.max(img) - np.min(img)))
    res = res.astype('uint8')
    return res

def gray_level(img, minimum, maximum, background=True):
    return np.where((img >= minimum) & (img <= maximum), 255, img if background else 0).astype('uint8')


def bit_plane_slicing(img, i):
    BITS = 8
    bin_mat = np.unpackbits(img,axis=0)

    bin_mat = bin_mat[i::8] * 255
    return bin_mat









img = cv2.imread('soldier.jpg', cv2.IMREAD_GRAYSCALE)
img_negated = negation(img)
img_thresholded = thresholding(img, 200).astype('uint8')
img_contrast_stretched = contrast_stretching(img)
img_gray_level = gray_level(img, 50,100, False)
img_plane_slicing = bit_plane_slicing(img, 2)

cv2.imshow("originial", img)
cv2.imshow("negated", img_negated)
cv2.imshow("thresholded", img_thresholded)
cv2.imshow("contrast stretched", img_contrast_stretched)
cv2.imshow("gray level slicing", img_gray_level)
cv2.imshow("bit slicing", img_plane_slicing)
cv2.waitKey(0)
cv2.destroyAllWindows()