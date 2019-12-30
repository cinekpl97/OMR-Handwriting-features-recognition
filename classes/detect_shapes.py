# import the necessary packages
from classes.shapedetector import ShapeDetector
import argparse
import imutils
import cv2
import numpy as np


def detect_frame_coordinates(image):
    resized_image = imutils.resize(image, width=1500)
    ratio = image.shape[0] / float(resized_image.shape[0])
    # convert the resized image to grayscale, blur it slightly,
    # and threshold it
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # loop over the contours
    for c in cnts:
        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(c)
        if w > 50 and h > 50:
            black_white_recognized_image = image[y:y + h, x:x + w]

    # cv2.imshow("Cropped image black/white", black_white_recognized_image)
    cv2.waitKey(0)
    x += 6
    y += 5
    w -= 20
    h -= 18
    return x, y, w, h
