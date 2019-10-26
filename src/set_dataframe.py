import re
import os
import pandas as pd
import numpy as np
from get_data import get_picture_per_classes, get_image_name, get_classes_from_images, get_image, get_parental_path

classes = os.listdir('../data/input_images')


# Entire list of the pictures:
images = get_picture_per_classes(classes)

# Name of the image:
images_name = [get_image_name(item) for image in images for item in image]

# Get the images classes_
image_classes = [get_classes_from_images(item) for item in images_name]

# Prepare a dictionary for further DataFrame:
new_dict = {'Images_name':images_name, 'Image_class': image_classes}

# First approach to final DataFrame:
p = pd.DataFrame(new_dict, index=images_name, columns=['Image_class'])

# Dummified DataFrame per classes
new_p = pd.get_dummies(p['Image_class'])

# First DataFrame
new_p.to_csv(r'../images_dummies.csv')

