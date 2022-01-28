import cv2
import os
import numpy

def equalizeHistogram (image, factor):
    image2 = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    height, width, channels = image2.shape
    array = []
    for i in range(0, 256):
        array.append(0)
    for x in range(0, height):
        for y in range(0, width):
            index = image2[x,y,1]
            array[index] += 1
            minIndex = 0
            maxIndex = 255
            if index - factor > 0:
                minIndex = index - factor
            if index + factor < 255:
                maxIndex = index + factor
            rangeForMin = array[(minIndex):(maxIndex+1)]
            min = numpy.argmin(rangeForMin) + (minIndex)
            image2[x,y,1] = min
    image2 = cv2.cvtColor(image2, cv2.COLOR_HLS2BGR)
    return image2

if (os.path.isdir('./Resources/images/hist1')==False):
		#kreiraj folder
		os.mkdir('./Resources/images/hist1')

for i in range(853):
    # Učitavanje slike
    img = cv2.imread('./Resources/images/brightness2/maksssksksss' + str(i) + '.png')
    dst = equalizeHistogram(img, 30)
    print(i)
    # Pohranjivanje slike
    cv2.imwrite('./Resources/images/hist1/maksssksksss' + str(i) + '.png', dst)