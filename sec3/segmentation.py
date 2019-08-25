import scipy.ndimage as nd
import numpy as np
import cv2


def roberts(img):
    img = img.astype(np.float32)
    x_kernel = np.array([[1,0], [0,-1]]).astype(np.float32)
    y_kernel = np.array([[0,1], [-1,0]]).astype(np.float32)
    Gx = nd.convolve(img, x_kernel.astype(np.float32), mode='constant')
    Gy = nd.convolve(img, y_kernel.astype(np.float32), mode='constant')
    G = np.sqrt(Gx ** 2 + Gy ** 2).astype('uint8')
    # cv2.imshow("Roberts", G)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return G


def sobel(img):
    img = img.astype(np.float32)
    img = cv2.GaussianBlur(img,(5,5), 1.3)
    x_kernel = np.array([[-1, 0, 1],[-2, 0, 2], [-1, 0, 1]]).astype(np.float32)
    y_kernel = x_kernel.T
    # y_kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]).astype(np.float32)
    Gx = nd.convolve(img, x_kernel.astype(np.float32), mode='constant')
    Gy = nd.convolve(img, y_kernel.astype(np.float32), mode='constant')
    G = np.sqrt((Gx ** 2 + Gy ** 2)).astype(np.uint8)
    # cv2.imshow("origin", img)
    # cv2.imshow("Sobel", G)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return G


def prewwit(img):
    img = img.astype(np.float32)
    img = cv2.GaussianBlur(img,(3,3), 1.3)
    x_kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    y_kernel = x_kernel.T

    Gx = nd.convolve(img, x_kernel.astype(np.float32), mode='constant')
    Gy = nd.convolve(img, y_kernel.astype(np.float32), mode='constant')
    G = np.sqrt((Gx ** 2 + Gy ** 2)).astype(np.uint8)
    # cv2.imshow("origin", img)
    # cv2.imshow("Prewit", G)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return G


img = cv2.imread("bike.jpg", cv2.IMREAD_GRAYSCALE)
img1 = roberts(img)
img2 = sobel(img)
img3 = prewwit(img)

cv2.imshow("original", img)
cv2.imshow("Roberts", img1)
cv2.imshow("Sobel", img2)
cv2.imshow("Prewitt", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()