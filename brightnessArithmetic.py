import cv2
import numpy as np
import os

def increaseBrightness (image, factor):
    im2 = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    height, width, channels = im2.shape
    for x in range(0, height):
        for y in range(0, width):
            if im2[x,y,1] < 255 - factor:
                im2[x,y,1] += factor
    return cv2.cvtColor(im2, cv2.COLOR_HLS2BGR)

if (os.path.isdir('./Resources/images/brightness1')==False):
		#kreiraj folder
		os.mkdir('./Resources/images/brightness1')

for i in range(853):
    # Učitavanje slike
    img = cv2.imread('./Resources/images/contrast2/maksssksksss' + str(i) + '.png')
    dst = increaseBrightness(img, 30)
    print(i)
    # Pohranjivanje slike
    cv2.imwrite('./Resources/images/brightness1/maksssksksss' + str(i) + '.png', dst)