import cv2
import os

if (os.path.isdir('./Resources/images/brightness3')==False):
		#kreiraj folder
		os.mkdir('./Resources/images/brightness3')

for i in range(853):
    # Učitavanje slike
    img = cv2.imread('./Resources/images/contrast2/maksssksksss' + str(i) + '.png')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    value = 40
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    print(i)
    # Pohranjivanje slike
    cv2.imwrite('./Resources/images/brightness3/maksssksksss' + str(i) + '.png', img)