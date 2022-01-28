import numpy as np
import cv2
import os


def gammaContrast(image, gamma):
    g = 1.0 / gamma
    table = np.array([((i / 255.0) ** g) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)


if (os.path.isdir('./Resources/images/contrast3')==False):
		#kreiraj folder
		os.mkdir('./Resources/images/contrast3')

for i in range(853):
    # Učitavanje slike
    img = cv2.imread('./Resources/images/denoise_sharpen/maksssksksss' + str(i) + '.png')
    dst = gammaContrast(img, 0.7)
    print(i)
    # Pohranjivanje slike
    cv2.imwrite('./Resources/images/contrast3/maksssksksss' + str(i) + '.png', dst)