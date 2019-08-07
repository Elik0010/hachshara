import numpy as np
import matplotlib.pyplot as plt
import math
import imageio
import scipy
from skimage import restoration, util


def to_gray(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i,j] = np.dot(img[i,j], [0.2989, 0.5870, 0.1140])
    
    return img[:,:,0]
'''
def non_local_means(img_file):
    img = imageio.imread(img_file)

    img = to_gray(img)

    img_noise = util.random_noise(img, 's&p', amount=0.03)

    img_denoise_1_1 = restoration.denoise_nl_means(img_noise, patch_size=7, patch_distance=20)

    img_denoise_1_2 = restoration.denoise_nl_means(img_noise, patch_size=7, patch_distance= 30)


    img_denoise_1_3 = restoration.denoise_nl_means(img_noise, patch_size=7, patch_distance=10)

    img_denoise_2_1 = restoration.denoise_nl_means(img_noise, patch_size=3, patch_distance=20)

    img_denoise_2_2 = restoration.denoise_nl_means(img_noise, patch_size=7, patch_distance=20)

    img_denoise_2_3 = restoration.denoise_nl_means(img_noise, patch_size=11, patch_distance=20)

    

    f, axx = plt.subplots(2,5)
    axx[0,0].imshow(img, cmap='gray')
    axx[0,0].set_title("Original")

    axx[0,1].imshow(img_noise, cmap='gray')
    axx[0,1].set_title("Noisy")

    axx[0,2].imshow(img_denoise_1_1, cmap='gray')
    axx[0,2].set_title("Cleaned dist 20")

    axx[0,3].imshow(img_denoise_1_2, cmap='gray')
    axx[0,3].set_title("Cleaned dist 30")

    axx[0,4].imshow(img_denoise_1_3, cmap='gray')
    axx[0,4].set_title("Cleaned dist 10")

    axx[1,0].imshow(img, cmap='gray')
    axx[1,0].set_title("Original")

    axx[1,1].imshow(img_noise, cmap='gray')
    axx[1,1].set_title("Noisy")
    
    axx[1,2].imshow(img_denoise_2_1, cmap='gray')
    axx[1,2].set_title("cleaned patch 3")

    axx[1,3].imshow(img_denoise_2_2, cmap='gray')
    axx[1,3].set_title("cleaned patch 7")
    
    axx[1,4].imshow(img_denoise_2_3, cmap='gray')
    axx[1,4].set_title("cleaned patch 11")

    
    plt.show()
'''



def f_func(img, i, j, x, y):
    hood_this = img[i - 1: i + 2, j - 1: j + 2]
    hood_other = img[x - 1: x + 2, y - 1: y + 2]
    B_this = np.mean(hood_this)
    B_other = np.mean(hood_other)
    variance = np.var(hood_this)
    f = np.exp(-(abs(B_other - B_this) ** 2) / np.sqrt(variance))
    #print(f)   
    return f 

def c_func(img, i, j):
    result = []
    for index, x in np.ndenumerate(img):
        result.append(f_func(img, i, j, index[0], index[1]))
    return sum(result)

def my_non_local_means(img_file):
    img = imageio.imread(img_file)

    img = to_gray(img)
    img = np.pad(img, 1, 'constant', constant_values=0)
    img_noise = util.random_noise(img, 's&p', amount=0.01)

    cleaned_image = img_noise.copy()  

    for indices, _ in img_noise:
        result = []
        for index, _ in img_noise
            result.append(f_func(img_noise, indices[0], indices[1], index[0], index[1]))
        cleaned_image[i,j] = (1 / c_func(img_noise, i, j)) * sum(result)
    f, xx = plt.subplots(1,4)
    xx[0].imshow(img)
    xx[1].imshow[img_noise]
    xx[2].imshow[cleaned_image]
                

#TEST CODE
test_file = 'icon.jpg'
my_non_local_means(test_file)




