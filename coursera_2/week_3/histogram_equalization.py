import numpy as np
import math
import matplotlib.pyplot as plt
import skimage
import imageio

def to_gray(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i,j] = np.dot(img[i,j], [0.2989, 0.5870, 0.1140])
    
    return img[:,:,0]

def histogram_equalisation(img_file):
    img = imageio.imread(img_file)
    img = skimage.data.camera()
    if len(img.shape) == 3:
        img = to_gray(img)

    f, xrr= plt.subplots(2,2)
    xrr[0,1].imshow(img, cmap='gray')
    xrr[0,0].hist(img)
    new_img = []
    probability = np.bincount(img.flatten()) / img.size #takes the amount of each intensity in relation to total number of pixels
    SHADES = 256
    for value in np.nditer(img):
        total = 0
        for k in range(value):
            total = total + probability[k]
        new_img.append(math.floor((SHADES - 1) * sum(probability[:value])))
    new_img = np.array(new_img).reshape(img.shape)
    xrr[1,0].hist(new_img)
    xrr[1,1].imshow(new_img, cmap='gray')
    plt.show()
    return new_img

#TEST CODE
test_file = 'terror.jpg'
print(histogram_equalisation(test_file))

