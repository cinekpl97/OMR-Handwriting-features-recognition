import argparse

import cv2 as cv
import numpy as np
import time
import imutils
from classes.detect_shapes import detect_frame_coordinates


def take_frame_out_of_image(frame):
    cropped_image_original = frame[int(frame.shape[0] / 2):int(frame.shape[0] / 2 + frame.shape[0] / 10),
                             50:int(frame.shape[1] - frame.shape[1] / 10)]
    cropped_image_black_white = cropped_image_original.copy()
    gray = cv.cvtColor(cropped_image_black_white, cv.COLOR_BGR2GRAY)

    ret, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
    cropped_image_black_white[thresh == 255] = 0
    cropped_image_black_white[thresh == 0] = [255, 255, 255]
    contours, h = cv.findContours(thresh, 1, 2)

    # printing paper sheet in smaller size
    scale = 30
    widthscale = int(cropped_image_black_white.shape[1] * scale / 100)
    heightscale = int(cropped_image_black_white.shape[0] * scale / 100)

    dim = (widthscale, heightscale)

    cropped_image_frame_original = cv.resize(cropped_image_original, dim, interpolation=cv.INTER_AREA)
    resized_image_black_white = cv.resize(cropped_image_black_white, dim, interpolation=cv.INTER_AREA)
    cv.imwrite('D:\\PROGRAMOWANIE\\Python programy\\untitled\\test_image.jpg', resized_image_black_white)
    cv.imshow('Resized black and white', resized_image_black_white)
    x, y, w, h = detect_frame_coordinates(resized_image_black_white)
    cropped_image_frame_original = cropped_image_frame_original[y:y + h, x:x + w]
    cv.imshow('Cropped image frame original', cropped_image_frame_original)
    cv.imwrite('example.jpeg', cropped_image_frame_original)

    cv.waitKey(0)
    cv.destroyAllWindows()
