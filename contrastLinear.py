import numpy
import os
import cv2

from PIL import Image

def normalizeRed(intensity):
    iI = intensity
    minI = 60
    maxI = 215
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO


def normalizeGreen(intensity):
    iI = intensity
    minI = 50
    maxI = 215
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO


def normalizeBlue(intensity):
    iI = intensity
    minI = 50
    maxI = 215
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO

def increaseContrast (image):
    pil_im = Image.fromarray(image)
    multiBands = pil_im.split()

    normalizedRedBand = multiBands[2].point(normalizeRed)
    normalizedGreenBand = multiBands[1].point(normalizeGreen)
    normalizedBlueBand = multiBands[0].point(normalizeBlue)

    new_pil_im = Image.merge("RGB", (normalizedRedBand, normalizedGreenBand, normalizedBlueBand))
    im2 = cv2.cvtColor(numpy.array(new_pil_im), cv2.COLOR_RGB2BGR)

    return im2

if (os.path.isdir('./Resources/images/contrast2')==False):
		#kreiraj folder
		os.mkdir('./Resources/images/contrast2')

for i in range(853):
    # Učitavanje slike
    img = cv2.imread('./Resources/images/denoise_sharpen/maksssksksss' + str(i) + '.png')
    dst = increaseContrast(img)
    print(i)
    # Pohranjivanje slike
    cv2.imwrite('./Resources/images/contrast2/maksssksksss' + str(i) + '.png', dst)
