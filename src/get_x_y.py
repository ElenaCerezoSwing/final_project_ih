import re
import os
import cv2
import pandas as pd
import numpy as np
from get_data import get_parental_path, get_array



def get_images_and_wastes():
    new_p = pd.read_csv('../images_dummies.csv') 
    new_p['image'] = new_p.index

    images=[]
    wastes=[]
    for row, index_row in new_p.iterrows():
        # get the images root
        image_root = get_parental_path(row)
        # read the image
        read_image = cv2.imread(ROOT_IMG + image_root)
        # image processing
        gray_image = cv2.cvtColor(read_image, cv2.COLOR_BGR2GRAY)
        resized_img = cv2.resize(gray_image, None, fx=0.5, fy=0.5)
        expanded_dim = np.expand_dims(resized_img, axis=2)
        # images appendize
        images.append(expanded_dim)
        
        # get array of wastes types values per image
        wastes.append(get_array(new_p['cardboard'][row], new_p['glass'][row], new_p['metal'][row], 
                new_p['paper'][row], new_p['plastic'][row], new_p['trash'][row]))

    return images, wastes

