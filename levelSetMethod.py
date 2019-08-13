import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import scipy



'''
for the purposes of the functions below, phi will need to be in the form of a matrix
'''


def PDE(phi, F):

    dt = 1
    it = 5

    #dt * dphi = phi(t + dt) - phi(t)
    #dt * dphi + phi(t) = phi(t + dt)
    #phi(t + dt) = phi(t) + dt * F * dphi_norm
    _, xx = plt.subplots(1,5)
    for i in  range(it):
        dphi = np.array(np.gradient(phi))
        dphi_norm = np.sqrt(np.sum(dphi ** 2, axis=0))
        phi = phi + dt * F * dphi_norm
        
        xx[i].contour(phi, 0)
    plt.show()






def curve_flow(phi, F):
    ds = 1
    it = 5

    _, xx = plt.subplots(1,5)
    for i in range(it):
        #based on https://en.wikipedia.org/wiki/Mean_curvature_flow
        # Find S Arc Length





        #find ds_dx and ds_dy
        ds_dx, ds_dy = np.gradient(phi)


        #Define D
        D = 1


        #find dds_dxx, dds_dxdy and dds_dyy
        dds_dxx, dds_dxdy = np.gradient(ds_dx)
        dds_dyy = np.gradient(ds_dy, axis=1)



        #find H
        numer = 0.5 * (1 + ds_dx ** 2) * dds_dyy - 2 * ds_dx * ds_dy * dds_dxdy + (1 + ds_dy ** 2) * dds_dxx
        denom = (1 + ds_dx ** 2 + ds_dy ** 2) ** (3/2)

        H = numer / denom

        #find ds/dt
        ds_dt = 2 * D * H * np.sqrt(1 + ds_dx ** 2 + ds_dy ** 2)


        #apply to phi
        # phi = phi + ds * F * ds_dt
        dphi = np.array(np.gradient(phi))
        dphi_norm = np.sqrt(np.sum(dphi ** 2, axis=0))
        phi = phi + ds_dt * F * dphi_norm
        xx[i].contour(phi, 0)
    plt.show()



#TEST CODE
# F = lambda x: x ** 2
F = 0.5


phi = cv2.imread('terror.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow("sdsd",phi)
# phi = np.random.normal(30,30)
phi = np.random.normal(size=(30,30))


PDE(phi, F)

curve_flow(phi, F)