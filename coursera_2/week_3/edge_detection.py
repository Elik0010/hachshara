import numpy as np
import matplotlib.pyplot as plt
import imageio
import scipy.signal


def color_edge_detection(img_file):
    img = imageio.imread(img_file)
    img_r = img[:,:,0]
    img_g = img[:,:,1]
    img_b = img[:,:,2]

    horaz_kernel = [[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]]
    verti_kernel = [[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]]

    der_horizontal_r = scipy.signal.convolve2d(horaz_kernel, img_r)
    der_vertical_r = scipy.signal.convolve2d(verti_kernel, img_r)
    der_r = der_horizontal_r + der_vertical_r

    der_horizontal_g = scipy.signal.convolve2d(horaz_kernel, img_g)
    der_vertical_g = scipy.signal.convolve2d(verti_kernel, img_g)
    der_g = der_horizontal_g + der_vertical_g

    der_horizontal_b = scipy.signal.convolve2d(horaz_kernel, img_b)
    der_vertical_b = scipy.signal.convolve2d(verti_kernel, img_b)
    der_b = der_horizontal_b + der_vertical_b

    f, xx = plt.subplots(1,4)

    xx[0].imshow(der_r)
    xx[1].imshow(der_g)
    xx[2].imshow(der_b)
    xx[3].imshow(der_r + der_b + der_g, cmap='hsv')

    plt.show()

#TEST CODE
test_file = 'camo.jpg'
color_edge_detection(test_file)
