import numpy as np
import math
import cv2



def point_dct(img):
    res = np.zeros(img.shape)
    # for i in range(img.shape[0]):
    #     for j in range(img.shape[1]):
    #         sub_res = np.zeros(img.shape)
    #         for x in range(img.shape[0]):
    #             for y in range(img.shape[1]):
    #                 sub_res[x,y] = img[x,y] * math.cos((math.pi / img.shape[0]) * (x + .5) * i) \
    #                     * math.cos((math.pi / img.shape[1]) * (y + 0.5) * j)
    #         res[i,j] = np.sum(sub_res)
    # return res
    rows, cols = img.shape
    for i in range(rows):
        for j in range(cols):
            cos1 = np.cos((np.pi / rows) * (np.arange(rows) + 0.5) * i)
            cos2 = np.cos((np.pi / cols) * (np.arange(cols) + 0.5) * j)
            sub_res =  img * np.outer(np.transpose(cos1),cos2)
            # sub_res =  np.outer(cos1,cos2)
            res[i,j] = np.sum(sub_res)
    return res

    # res = np.zeros(img.shape)
    # for k in range(img.shape[1]):
    #     res[0,k] = 1 / np.sqrt(img.shape[1])
    # for i in range(1, img.shape[0]):
    #     for j in range(img.shape[1]):
    #         res[i,j] = math.sqrt(2 / img.shape[1]) * np.cos((math.pi * (2 * j + 1) * i) / (2 * img.shape[1]))
    #         # res[i,j] = math.cos(math.pi/img.shape[1] * i * (j + 0.5))
    # # print(res)
    # return res


def point_dst(img):
    rows,cols = img.shape
    #SLOW
    res = np.zeros(img.shape)
    for i in range(rows):
        for j in range(cols):
            sub_res = np.zeros(img.shape)

            sin1 = np.transpose(np.sin((np.pi/rows) * (i + 0.5) * (np.arange(rows) + 1)))
            sin2 = np.sin((np.pi/cols) * (j + 0.5) * (np.arange(cols) + 1))
            # sub_res = img * np.outer(sin1, sin2)
            sub_res = np.outer(sin1,sin2)
            res[i,j] = np.sum(sub_res)
    return res
    #SUPER SLOW
    for i in range(rows):
        for j in range(cols):
            sub_res = np.zeros(img.shape)
            for x in range(rows):
                for y in range(cols):
                    sin1 = np.sin((np.pi/rows) * (i + 0.5) * (x + 1))
                    sin2 = np.sin((np.pi / rows) * (j + 0.5) *  (y + 1))
                    sub_res[x,y] = img[x,y] * sin1 * sin2
            res[i,j] = np.sum(sub_res)
    return res

    # #TYPE 1 (ALSO SLOW)
    # for i in range(rows):
    #     for j in range(cols):
    #         for x in range(rows):
    #             for y in range(cols):
                    

def DCT_IDCT(img_file):
    # img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
    img = np.arange(400).reshape((20,20))
    # cv2.imshow("original", img)
    # cv2.waitKey(0)
    # img = np.pad(img,20,'constant', constant_values=0)
    # img[1::2,::2] = 1
    # img[::2,1::2] = 1    
    img = np.array(img, dtype='uint8')
    # print(img)
    #DCT
    cv2.imshow("origin", img)
    cv2.waitKey(0)
    res = point_dct(img)
    img = res #* img * np.transpose(res)
    print(img)
    #IDCT
    # img = np.transpose(res) * img * res
    print(img)

    img = cv2.resize(img, (300,300))
    cv2.imshow("final", img)
    cv2.waitKey(0)


def DST_IDST(img_file):
    # img = cv2.imread(img_file)
    img = np.ones(900).reshape((30,30))

    res = point_dst(img)
    cv2.imshow("final", cv2.resize(res, (300,300)))
    cv2.waitKey(0)



    

img_file = 'soldier.jpg'
DCT_IDCT(img_file)






