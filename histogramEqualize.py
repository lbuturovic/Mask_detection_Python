import cv2
import os

if (os.path.isdir('./Resources/images/hist3')==False):
		#kreiraj folder
		os.mkdir('./Resources/images/hist3')

for i in range(853):
    # Učitavanje slike
    img = cv2.imread('./Resources/images/brightness2/maksssksksss' + str(i) + '.png')
    for j in range(0, 3):
        img[:, :, j] = cv2.equalizeHist(img[:, :, j])
    print(i)
    # Pohranjivanje slike
    cv2.imwrite('./Resources/images/hist3/maksssksksss' + str(i) + '.png', img)