import re
import os
import pandas as pd


classes = os.listdir('../data/input_images')

def get_picture_per_classes(classes):
    return [os.listdir('../data/input_images/'+ item) for item in classes]

def get_image_name(item):
    return item.split('.')[0]

def get_classes_from_images(item):
    num = re.findall('\d+', item)
    return item.split(num[0])[0]

def get_image(item):
    return item + '.jpg'

def get_parental_path(item):
    parental = get_classes_from_images(item)
    return parental + '/'+ get_image(item)

def get_array(a, b, c, d, e, f): 
    return [a, b, c, d, e, f]   

