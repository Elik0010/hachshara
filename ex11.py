import math
import numpy as np
import matplotlib.pyplot as plt 
#11.1


def plotter():
    '''
    a,b is interval of plotting
    func is function of plotting
    '''
    xs = np.arange(0,2,0.0005)
    y = [(math.sin(x - 2) ** 2) * math.exp(-(x ** 2)) for x in xs]
    plt.plot(xs,y)
    
plotter()



#11.2
'''
mat = []
for i in range(10):
    temp = []
    for j in range(10):
        temp.append(np.random.randint(low=0, high = 100))
    mat.append(temp)
realb = None
estb = None
# z = np.random.normal(loc=0, scale=1, size=10)


b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
#Question blocked



#11.3
z = [np.random.randint(0,250) for i in range(10000)]
def histogram(z, bins):
    # mini = min(z)
    # maxi = max(z)

    # interval = (maxi - mini) // bins

    # intervals = np.zeros(bins, dtype = int)
    # for i in z:
    #     for j in range(bins, 0, -1):
    #         if i >= mini + j * interval:
    #             intervals += 1 
    
    plt.hist(z, bins=25)  
# plt.show()
histogram(z,25)
plt.show()