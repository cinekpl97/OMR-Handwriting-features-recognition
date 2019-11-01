import cv2 as cv
import numpy as np
from classes.handwriting_recognition import take_frame_out_of_image


def main():
    amount_of_polls = 6
    start_image_analysis(amount_of_polls)


def start_image_analysis(amount_of_polls):
    # image_path takes already filled polls
    for i in range(1, amount_of_polls + 1):
        image_path = f'images\\{i}.jpg'
        print(f'Chosen path: {image_path}')
        try:
            file = open(image_path)
            file.close()
            image = cv.imread(image_path)
            take_frame_out_of_image(image)
        except FileNotFoundError:
            print(f'file {image_path} not found')


if __name__ == '__main__':
    main()
