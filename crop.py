import os
import xml.etree.ElementTree as ET

import cv2
from keras_applications.densenet import preprocess_input
from keras_preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array

IMAGES_PATH = './Resources/images/contrast2/'
IMAGE_NAME = 'maksssksksss'
ANNOTATIONS_PATH = './Resources/annotations/'


def create_folder(path):
    if (os.path.isdir(path) == False):
        # kreiraj folder
        os.mkdir(path)


def get_objects(xml_file):
    annotation = ET.parse(xml_file)
    root = annotation.getroot()

    objects = []
    for obj in root.findall('object'):
        new_object = {'name': obj.find('name').text}
        bbox_tree = obj.find('bndbox')
        new_object['bbox'] = (int(bbox_tree.find('xmin').text),
                              int(bbox_tree.find('ymin').text),
                              int(bbox_tree.find('xmax').text),
                              int(bbox_tree.find('ymax').text),
                              )
        objects.append(new_object)
    return objects


create_folder('./Resources/images/cropped')
create_folder('./Resources/images/cropped/with_mask')
create_folder('./Resources/images/cropped/without_mask')
create_folder('./Resources/images/cropped/wrong_mask_wearing')
m = 1
wm = 1
wmw = 1
for i in range(853):
    objects = get_objects('{}{}{}.xml'.format(ANNOTATIONS_PATH, IMAGE_NAME, i))
    img_path = '{}{}{}.png'.format(IMAGES_PATH, IMAGE_NAME, i)
    img = cv2.imread(img_path)
    for object in objects:
        xmin, ymin, xmax, ymax = object['bbox']
        cropped_image = img[ymin:ymax, xmin:xmax]
        cropped_image = cv2.resize(cropped_image, (224, 224))
        if object['name'] == "with_mask":
            cv2.imwrite('./Resources/images/cropped/with_mask/{}.png'.format(str(m)), cropped_image)
            m = m + 1
        elif object['name'] == "without_mask":
            cv2.imwrite('./Resources/images/cropped/without_mask/{}.png'.format(str(wm)), cropped_image)
            wm = wm + 1
        else:
            cv2.imwrite('./Resources/images/cropped/wrong_mask_wearing/{}.png'.format(str(wmw)), cropped_image)
            wmw = wmw + 1

exit(1)
