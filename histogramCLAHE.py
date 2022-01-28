import cv2
import os

def equalizeHistogram (image, factor):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    lab_planes = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(factor, factor))
    lab_planes[0] = clahe.apply(lab_planes[0])
    lab = cv2.merge(lab_planes)
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

if (os.path.isdir('./Resources/images/hist2')==False):
		#kreiraj folder
		os.mkdir('./Resources/images/hist2')

for i in range(853):
    # Učitavanje slike
    img = cv2.imread('./Resources/images/brightness2/maksssksksss' + str(i) + '.png')
    dst = equalizeHistogram(img, 30)
    print(i)
    # Pohranjivanje slike
    cv2.imwrite('./Resources/images/hist2/maksssksksss' + str(i) + '.png', dst)