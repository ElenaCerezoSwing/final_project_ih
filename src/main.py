

import cv2
import numpy as np
import os
from extracting_frames import get_image
from photo_classifier import get_photo_classification
from garbage_solution import get_garbage_solution

def main():
    get_image()
    waste_type = get_photo_classification()
    solution = get_garbage_solution(waste_type)
    print(solution)


if __name__ == '__main__':
    main()