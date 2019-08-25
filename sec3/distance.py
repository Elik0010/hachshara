import numpy as np
import cv2



def four_connected_fig(img):
    pass




def eight_connected_fig(img):
    pass


def pixel_distances(pix1, pix2):
    #eucledian
    euc_dist = np.sqrt((pix1[0] - pix2[0]) ** 2 + (pix1[1] - pix2[1]) ** 2)
    print("Eucledian Distance: %s" % euc_dist)
    
    #manhattan distance
    man_dist = abs(pix1[0] - pix2[0]) + abs(pix1[1] - pix2[1])
    print("Manhattan Distance: %s" % man_dist)


    #minkowaski distance
    p = 2
    minko_dist = (np.sum([abs(pix1[i] - pix2[i]) ** p for i in np.arange(len(pix1))])) ** (1 / p)
    print("Minkowaski Dsitance: %s" % minko_dist)

    #8-connected distance
    eight_distance = max(abs(pix1[0] - pix2[0]), abs(pix1[1] - pix2[1]))
    print("8-Connected Distance: %s" % eight_distance)

def image_distances(img1, img2):
    print(np.sum((img2-img1) ** 2))



img1 = cv2.imread('soldier.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('soldier.jpg', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('terror.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, np.transpose(img1).shape)
pix1 = (10,53)
pix2 = (39,103)

pixel_distances(pix1,pix2)
image_distances(img1,img2)
