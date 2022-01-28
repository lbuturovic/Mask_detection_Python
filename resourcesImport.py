import xml.etree.ElementTree as ET
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
import cv2

ANNOTATIONS_PATH = './Resources/annotations/'
IMAGES_PATH = './Resources/images/hist3/'
IMAGE_NAME = 'maksssksksss'


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


def separate_labels_and_data(img_path, objects, labels, data):
    img = cv2.imread(img_path)
    for object in objects:
        xmin, ymin, xmax, ymax = object['bbox']
        cropped_image = img[ymin:ymax, xmin:xmax]
        cv2.imwrite('./Resources/images/pomocna.png', cropped_image)
        cropped_image = cv2.resize(cropped_image, (224, 224))
        cropped_image = img_to_array(cropped_image)
        cropped_image = preprocess_input(cropped_image)
        labels.append(object['name'])
        data.append(cropped_image)


def get_labels_and_data():
    labels = []  # labele svakog objekta
    data = []  # data predstavlja fotografije objekata odsjecenih iz dataseta
    for i in range(853):
        objects = get_objects('{}{}{}.xml'.format(ANNOTATIONS_PATH, IMAGE_NAME, i))
        img_path = '{}{}{}.png'.format(IMAGES_PATH, IMAGE_NAME, i)
        separate_labels_and_data(img_path, objects, labels, data)
    return labels, data
