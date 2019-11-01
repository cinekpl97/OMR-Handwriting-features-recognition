import argparse

import cv2 as cv
import numpy as np
import time
import imutils
from classes.detect_shapes import detect_frame_coordinates


def take_frame_out_of_image(frame):
    cropped_x1 = int(frame.shape[0] / 1.8)
    cropped_x2 = int(frame.shape[0] / 1.5 + frame.shape[0] / 8)
    cropped_y1 = 50
    cropped_y2 = int(frame.shape[1] - frame.shape[1] / 30)

    cropped_image_original = frame[cropped_x1:cropped_x2, cropped_y1:cropped_y2]

    cropped_image_black_white = cropped_image_original.copy()

    gray = cv.cvtColor(cropped_image_black_white, cv.COLOR_BGR2GRAY)

    ret, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
    # setting white to black
    cropped_image_black_white[thresh == 255] = 0
    # setting black to white - image before change
    cropped_image_black_white[thresh == 0] = [255, 255, 255]

    # printing paper sheet in smaller size
    scale = 20
    widthscale = int(cropped_image_black_white.shape[1] * scale / 100)
    heightscale = int(cropped_image_black_white.shape[0] * scale / 100)

    dim = (widthscale, heightscale)

    cropped_image_frame_original = cv.resize(cropped_image_original, dim, interpolation=cv.INTER_AREA)
    resized_image_black_white = cv.resize(cropped_image_black_white, dim, interpolation=cv.INTER_AREA)

    cv.imshow('Resized black and white', resized_image_black_white)
    x, y, w, h = detect_frame_coordinates(resized_image_black_white)
    cropped_image_frame_original = cropped_image_frame_original[y:y + h, x:x + w]
    cv.imshow('Cropped image frame original', cropped_image_frame_original)

    cv.waitKey(0)
    cv.destroyAllWindows()
