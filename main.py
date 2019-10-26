import cv2 as cv
import numpy as np
from classes.handwriting_recognition import take_frame_out_of_image


def main():
    for i in range(3, 4):
        image_path = f'images\\proba{i}.jpg'
        print(image_path)
        frame = cv.imread(image_path)
        take_frame_out_of_image(frame)


if __name__ == '__main__':
    main()