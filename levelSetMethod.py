import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import cv2
import math
import scipy


def write(*i):
    f = open("temp.txt","w+")
    for j in i:
        f.write(str(j) + "\n\n\n\n")

def PDE(phi, F):

    dt = 1
    it = 5

    #dt * dphi = phi(t + dt) - phi(t)
    #dt * dphi + phi(t) = phi(t + dt)
    #phi(t + dt) = phi(t) + dt * F * dphi_norm
    _, xx = plt.subplots(1,5)
    for i in  range(it):
        dphi = np.array(np.gradient(phi))
        # normal = -dphi / np.linalg.norm(dphi)
        # k_curvature = np.linalg.norm(dphi)
        dphi_norm = np.sqrt(np.sum(dphi ** 2, axis=0))
        phi = phi + dt * dphi_norm * F
        xx[i].contour(phi, 0)
    plt.show()

    





'''
def curve_flow(phi):
    ds = 1
    it = 50

    # _, xx = plt.subplots(1,5)
    for i in range(it):
        #based on https://en.wikipedia.org/wiki/Mean_curvature_flow
        # Find S Arc Length





        #find ds_dx and ds_dy
        ds_dx, ds_dy = np.gradient(phi)


        write(ds_dx, ds_dy)
        #Define D
        D = 1


        #find dds_dxx, dds_dxdy and dds_dyy
        dds_dxx, dds_dxdy = np.gradient(ds_dx)
        dds_dyy = np.gradient(ds_dy, axis=1)



        #find H
        numer = 0.5 *( (1 + ds_dx ** 2) * dds_dyy - 2 * ds_dx * ds_dy * dds_dxdy + (1 + ds_dy ** 2) * dds_dxx)
        denom = (1 + ds_dx ** 2 + ds_dy ** 2) ** 1.5

        H = numer / denom

        #find ds/dt
        ds_dt = 2 * D * H * np.sqrt(1 + ds_dx ** 2 + ds_dy ** 2)


        #apply to phi
        # phi = phi + ds * F * ds_dt
        dphi = np.array(np.gradient(phi))
        dphi_norm = np.sqrt(np.sum(dphi ** 2, axis=0))
        phi = phi + ds_dt * D * dphi_norm
        # xx[i].contour(phi, 0)
        plt.contour(phi, 0 )
        plt.show()
    # plt.show()
'''


def curve_flow(phi):

    ds = 5    
    it = 50
    # _, xx = plt.subplots(1,5)
    for i in range(it):

        #find tangent (dx_dt, dy_dt)
        dx_dt, dy_dt = np.gradient(phi)

        write(dx_dt, dy_dt, np.sqrt(np.sum(phi ** 2)), phi)

        #ds_dy and ds_dx


        T = np.sqrt(dx_dt ** 2 + dy_dt ** 2)
        unit = np.linalg.norm(T)
        T = T / unit

        #find ddy_dtt, ddx_dtt
        ddx_dtt = np.gradient(dx_dt)[0]
        ddy_dtt = np.gradient(dy_dt)[1]

        #find curvature dT_ds or k 
        k_numer = dx_dt * ddy_dtt - dy_dt * ddx_dtt
        k_numer2 = np.linalg.norm(k_numer)

        k_denom = (dx_dt ** 2 + dy_dt ** 2) ** (3/2)
        k = k_numer / k_denom
        k = np.nan_to_num(k)
        
        dphi = np.array(np.gradient(phi))
        ddphi = np.array(np.gradient(phi))
        dphi_norm = np.sqrt(np.sum(dphi**2, axis=0))
        
        #TEMP
        k = np.array(np.gradient(dphi_norm))
        k = np.linalg.norm(k, axis=0)


        # k = np.linalg.norm(dphi)
        phi = phi + k * dphi_norm * ds
        # xx[i].contour(phi, 0)
        plt.contour(phi, 0)
        plt.show()
    # plt.show()



'''
def curve_flow(phi):
    dt = 1
    it = 50

    for i in range(it):
        dphi = np.array(np.gradient(phi))
        dphi_norm = np.sqrt(np.sum(dphi ** 2, axis=0))
        curve = np.where(phi == 0)
        dx_ds, dy_ds = np.gradient(curve)

        curve_norm = np.linalg.norm(curve, axis=0)


        ddx_dss = np.gradient(dx_ds)[0]
        ddy_dss = np.gradient(dy_ds)[0]

        k = np.linalg.norm((dx_ds * ddy_dss - dy_ds * ddx_dss)) / (dx_ds ** 2 + dy_ds ** 2) ** (3/2)
        np.nan_to_num(k)
        
        phi = phi + dt * dphi_norm * k 
        plt.contour(phi, 0)
        plt.show()
'''

#TEST CODE
# F = lambda x: x ** 2
F = 0.05



# phi = cv2.imread('Black_Circle.jpg', cv2.IMREAD_GRAYSCALE)
# phi = cv2.imread('star.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow("sdsd",phi)
# phi = np.random.normal(30,30)
# phi = np.random.normal(size=(10,10))


phi = np.ndarray((3,3))
phi.fill(20)
phi = np.pad(phi, 2 , 'constant', constant_values=0)
# phi = np.pad(phi, 19 , 'constant', constant_values=5)


# PDE(phi, F)

curve_flow(phi)