import numpy as np
import cv2

def discrete_wavelet_transform(img, cutoff_percentile):
    #low pass filter
    frequencies = np.fft.fft(img)
    cutoff = np.amax(frequencies) * cutoff_percentile
    frequencies_low = np.where(frequencies <= cutoff, frequencies, 0) #approx coefficients
    img_low = np.fft.ifft(frequencies_low)
    #high pass filter
    frequencies_high = np.where(frequencies >= cutoff, frequencies, 0) #details coefficients
    img_high = np.fft.ifft(frequencies_high)

    return img_low.astype('uint8'), img_high.astype('uint8')




img = cv2.imread('soldier.jpg', cv2.IMREAD_GRAYSCALE)

img_low1, img_high1 = discrete_wavelet_transform(img, 0.0000000000000000001)
img_low2, img_high2 = discrete_wavelet_transform(img, 0.1)


cv2.imshow("decomposition 1 low", img_low1)
cv2.imshow("decomposition 1 high", img_high1)
cv2.imshow("decomposition 2 low", img_low2)
cv2.imshow("decomposition 2 high", img_high2)
cv2.waitKey(0)
cv2.destroyAllWindows()