import numpy as np
import cv2


def erosion_binary(space, struc):
    mid = struc.shape[0] // 2
    rows, cols = space.shape
    #pad the space for scanning purposes
    space = np.pad(space, mid, 'constant', constant_values=0)
    res = np.zeros(space.shape)
    struc_l, struc_h = struc.shape
    for i in range(rows):
        for j in range(cols):
            if np.all((struc - space[i:i + struc_l, j:j + struc_h]) == 0) :
                res[i + mid,j + mid] = 1
    return res[mid:-mid,mid:-mid]
            

            


def erosion_grayscale(space, struc):
    mid = struc.shape[0] // 2
    rows, cols = space.shape
    space = np.pad(space, mid, 'constant', constant_values=255)
    res = np.zeros(space.shape)
    struc_l, struc_h = struc.shape
    for i in range(rows):
        for j in range(cols):
            res[i+ mid,j + mid] = np.amin(space[i:i + struc_l, j:j + struc_h])
    return res[mid:-mid,mid:-mid].astype('uint8')


def dilation_binary(space, struc):
    mid = struc.shape[0] // 2
    rows, cols = space.shape
    #pad the space for scanning purposes
    space = np.pad(space, mid, 'constant', constant_values=0)
    res = np.zeros(space.shape)
    struc_l, struc_h = struc.shape
    for i in range(rows):
        for j in range(cols):
            if(space[i + mid, j + mid]):
                res[i:i + struc_l, j:j + struc_h] = struc
    return res[mid:-mid,mid:-mid].astype('uint8')

def dilation_grayscale(space, struc):
    mid = struc.shape[0] // 2
    rows, cols = space.shape
    space = np.pad(space, mid, 'constant', constant_values=0)
    res = np.zeros(space.shape)
    struc_l, struc_h = struc.shape
    for i in range(rows):
        for j in range(cols):
            res[i+ mid,j + mid] = space[i:i + struc_l, j:j + struc_h].max()
    return res[mid:-mid,mid:-mid].astype('uint8')

def opening_binary(space, struc):
    return dilation_binary(erosion_binary(space,struc), struc)

def closing_binary(space, struc):
    return erosion_binary(dilation_binary(space, struc), struc)

def opening_grayscale(space, struc):
    return dilation_grayscale(erosion_grayscale(space, struc), struc)

def closing_grayscale(space, struc):
    return erosion_grayscale(dilation_binary(space,struc), struc)


#TEST CODE
img = cv2.imread('room.jpg', cv2.IMREAD_GRAYSCALE)
a = np.zeros((5,5))
a = np.pad(a, 3, "constant", constant_values=0)
b = np.ones((3,3))
a[5,5] = 1
a[3,7] = 1
print("\n\n\n")
# a = opening_binary(a,b)
for i in range(20):
    img = dilation_grayscale(img, b)
    print(img)
    print("\n\n\n")
cv2.imshow("dilated",img)
cv2.waitKey(0)
cv2.destroyAllWindows()