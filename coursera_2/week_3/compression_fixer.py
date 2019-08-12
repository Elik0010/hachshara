import numpy as np
import matplotlib.pyplot as plt
import cv2
import scipy
import skimage.restoration as rest
import PIL.Image as pimg
import io

def compress(img):
    '''
    compression of image to JPEG 
    to the point of artifacts
    '''


    buffer = io.BytesIO()
    

    img.save(buffer, "JPEG", quality = 15)
    return buffer


def restore(comp_img):
    '''
    restoration of image to an attempt of its former self
    from the compressed state
    '''
    comp_img = np.array(comp_img)

    rest_img = scipy.ndimage.filters.gaussian_filter(comp_img, 1)


    return rest_img




def my_main(img_file):

    img = pimg.open(img_file).convert('L')

    #take image and make into a stored buffer
    buffer = compress(img)
    comp_img = pimg.open(buffer)

    rest_img = restore(comp_img)

    _, xx = plt.subplots(1,3)
    xx[0].imshow(img, cmap='gray')
    xx[1].imshow(comp_img, cmap='gray')
    xx[2].imshow(rest_img, cmap='gray')
    plt.show()
    

img_file = 'soldier.jpg'
my_main(img_file)