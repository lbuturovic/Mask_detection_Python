import cv2
import numpy as np
import os

def increaseBrightness (image, factor):
    factorscaled = (factor / 100) + 1
    return cv2.convertScaleAbs(image, 1, factorscaled)

if (os.path.isdir('./Resources/images/brightness2')==False):
		#kreiraj folder
		os.mkdir('./Resources/images/brightness2')

for i in range(853):
    # Učitavanje slike
    img = cv2.imread('./Resources/images/contrast2/maksssksksss' + str(i) + '.png')
    dst = increaseBrightness(img, 20)
    print(i)
    # Pohranjivanje slike
    cv2.imwrite('./Resources/images/brightness2/maksssksksss' + str(i) + '.png', dst)