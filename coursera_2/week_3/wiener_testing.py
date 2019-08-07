import scipy
import numpy as np
import imageio
import cv2
import skimage
import matplotlib.pyplot as plt
from PIL import Image



def practice_with_wiener(img_file):
    img = imageio.imread(img_file)
    #img = skimage.data.camera()
    img = skimage.color.rgb2gray(img)
    dirty_image = skimage.util.random_noise(img, mode='gaussian', var=.001)
    

    cleaned_with_wiener = scipy.signal.wiener(dirty_image)



    cleaned_with_nlmeans = skimage.restoration.denoise_nl_means(dirty_image)
    f, xx = plt.subplots(1,4)

    xx[0].imshow(img, cmap='gray')
    xx[1].imshow(dirty_image, cmap='gray')
    xx[2].imshow(cleaned_with_wiener, cmap='gray')
    xx[2].set_title('wiener')

    xx[3].imshow(cleaned_with_nlmeans, cmap='gray')
    xx[3].set_title('nlmeans')


    plt.show()















#TEST CODE
img_file = 'soldier.jpg'
practice_with_wiener(img_file)