import numpy as np
import matplotlib.pyplot as plt
import imageio
from skimage import util
import cv2 


def to_gray(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i,j] = np.dot(img[i,j], [0.2989, 0.5870, 0.1140])
    
    return img[:,:,0]


def rand_noise_addition(img_file):
    img = imageio.imread(img_file)

    img = to_gray(img)

    f, x = plt.subplots(1,6)

    res1 = util.random_noise(img)
    res2 = util.random_noise(img)
    res3 = util.random_noise(img)
    res4 = util.random_noise(img)
    res5 = util.random_noise(img)
    res6 = util.random_noise(img)
    res7 = util.random_noise(img)
    res8 = util.random_noise(img)
    res9 = util.random_noise(img)
    # summ = cv2.addWeighted(res1,res2,res3,res4,res5)
    summ1 = res1 + res2 + res3 #+ res4 + res5 + res6 + res7 + res8 + res9
    summ2 = res1 + res2 + res3 + res4 + res5 #+ res6 + res7 + res8 + res9
    summ3 = res1 + res2 + res3 + res4 + res5 + res6 + res7 #+ res8 + res9
    summ4 = res1 + res2 + res3 + res4 + res5 + res6 + res7 + res8 + res9
    
    x[0].imshow(res1, cmap='gray')
    x[1].imshow(summ1, cmap='gray')
    x[2].imshow(summ2, cmap='gray')
    x[3].imshow(summ3, cmap='gray')
    x[4].imshow(summ4, cmap='gray')
    x[5].imshow(res2, cmap='gray')
    plt.show()



    










#TEST CODE
test_file = 'soldier.jpg'
rand_noise_addition(test_file)