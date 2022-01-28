import cv2
import os
#za otklanjanje šuma koristi se bilateralni filter
if (os.path.isdir('./Resources/images/denoise')==False):
		#kreiraj folder
		os.mkdir('./Resources/images/denoise')
for i in range(853):
    # Učitavanje slike
    img = cv2.imread('./Resources/images/maksssksksss' + str(i) + '.png')
    dst = cv2.bilateralFilter(img, 9, 75, 75)
    # Pohranjivanje slike
    cv2.imwrite('./Resources/images/denoise/maksssksksss' + str(i) + '.png', dst)
