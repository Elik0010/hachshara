import numpy as np
import matplotlib.pyplot as plt
import math
import imageio

def pepper(img, amt):
    for i in range(len(img)):
        for j in range(len(img[i])):
            a = np.random.random()
            if a >= 1- amt:
                img[i,j] = 0
            elif a <= amt:
                img[i,j] = 255
    return img

def to_gray(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i,j] = np.dot(img[i,j], [0.2989, 0.5870, 0.1140])
    return img[:,:,0]


def setup_hood(img, x, y, ws):
    x = x - ws // 2
    y = y - ws // 2
    result = []
    for i in range(x, x + ws):
        sub_result = []
        for j in range(y, y + ws):
            sub_result.append(img[i,j])
        result.append(sub_result)
    return result



def med_filter(img_file, window_size, amt):
    if not window_size % 2:
        print("window size needs to be odd")
        return 
    if not isinstance(amt,int) or amt > 99 or amt < 1:
        print("amt needs to be value between 1 and 99 inclusive")
        return
    img = imageio.imread(img_file)

    img = to_gray(img)

    img = pepper(img,amt / 100)  
    img = np.pad(img, window_size // 2, 'constant', constant_values=0)
    img_output = img.copy()
    for i in range(window_size // 2, len(img) - window_size // 2):
        for j in range(window_size // 2, len(img[i]) - window_size // 2):
            # hood = np.matmul(img[i-1:i+2, j-1:j+2], filter)
            # hood = img(i - 1: i + 2, j - 1: j + 2)
            hood = setup_hood(img, i, j, window_size)
            img_output[i,j] = np.median(hood)
    f, xxr = plt.subplots(2,2)
    xxr[0,0].imshow(img, cmap='gray')
    xxr[0,1].hist(img)
    xxr[1,1].hist(img_output)
    xxr[1,0].imshow(img_output, cmap='gray')
    plt.show()


#TEST CODE
test_file = 'soldier.jpg'
med_filter(test_file,3, 8)  #second input must be odd

