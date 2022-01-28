import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def increaseContrast (image, factor):
    im2 = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    mean = cv2.mean(im2)
    height, width, channels = im2.shape
    for x in range(0, height):
        for y in range(0, width):
            if im2[x,y,1] < mean[1] and im2[x,y,1] > factor:
                im2[x,y][1] -= factor
            if im2[x,y,1] > mean[1] and im2[x,y,1] < 255 - factor:
                im2[x,y,1] += factor
    return cv2.cvtColor(im2, cv2.COLOR_HLS2BGR)

if (os.path.isdir('./Resources/images/contrast1')==False):
		#kreiraj folder
		os.mkdir('./Resources/images/contrast1')
kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]])

for i in range(853):
    # Učitavanje slike
    img = cv2.imread('./Resources/images/denoise_sharpen/maksssksksss' + str(i) + '.png')
    dst = increaseContrast(img, 20)
    print(i)
    # Pohranjivanje slike
    cv2.imwrite('./Resources/images/contrast1/maksssksksss' + str(i) + '.png', dst)

exit(1)