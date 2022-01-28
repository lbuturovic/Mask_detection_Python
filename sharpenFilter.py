import cv2
import numpy as np
import os
if (os.path.isdir('./Resources/images/denoise_sharpen')==False):
		#kreiraj folder
		os.mkdir('./Resources/images/denoise_sharpen')
kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]])
for i in range(853):
    # Učitavanje slike
    img = cv2.imread('./Resources/images/denoise/maksssksksss' + str(i) + '.png')
    dst = cv2.filter2D(img, -1, kernel)
    print(i)
    # Pohranjivanje slike
    cv2.imwrite('./Resources/images/denoise_sharpen/maksssksksss' + str(i) + '.png', dst)
exit(1)