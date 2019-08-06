import numpy as np
import matplotlib.pyplot as plt
import math
import imageio

def pepper(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            a = np.random.random()
            if a >= 0.98:
                img[i,j] = 0
            elif a <= 0.02:
                img[i,j] = 255
    return img

def to_gray(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i,j] = np.dot(img[i,j], [0.2989, 0.5870, 0.1140])
    return img[:,:,0]

def med_filter(img_file):
    filter = np.identity(3, dtype=int)
    img = imageio.imread(img_file)

    img = to_gray(img)

    img = pepper(img)  
    img = np.pad(img, 1, 'constant', constant_values=0)
    img_output = img.copy()
    for i in range(1, len(img) - 1):
        for j in range(1, len(img[i]) - 1):
            # hood = np.matmul(img[i-1:i+2, j-1:j+2], filter)
            hood = img(i - 1: i + 2, j - 1: j + 2)
            img_output[i,j] = np.median(hood)
    f, xxr = plt.subplots(2,2)
    xxr[0,0].imshow(img, cmap='gray')
    xxr[0,1].hist(img)
    xxr[1,1].hist(img_output)
    xxr[1,0].imshow(img_output, cmap='gray')
    plt.show()


#TEST CODE
test_file = 'soldier.jpg'
med_filter(test_file)

