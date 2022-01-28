import cv2
import os
if (os.path.isdir('./Resources/images/blur')==False):
		#kreiraj folder
		os.mkdir('./Resources/images/blur')
for i in range(853):
    # Učitavanje slike
    img = cv2.imread('./Resources/images/maksssksksss' + str(i) + '.png')
    # Zamagljenje filterom 5x5 upotrebom funkcije blur
    dst = cv2.blur(img,(5,5))
    print(i)
    # Pohranjivanje slike
    cv2.imwrite('./Resources/images/blur/maksssksksss' + str(i) + '.png', dst)