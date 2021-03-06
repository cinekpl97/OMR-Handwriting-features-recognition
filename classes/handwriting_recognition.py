import cv2 as cv
import numpy as np
from classes.detect_shapes import detect_frame_coordinates


def recognize_word(im):
    # Params
    maxArea = 1000
    minArea = 5
    # Read image
    image = im.copy()
    # Convert to gray
    Igray = cv.cvtColor(im, cv.COLOR_RGB2GRAY)

    # Threshold
    ret, Ithresh = cv.threshold(Igray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    # Keep only small components but not to small
    comp = cv.connectedComponentsWithStats(Ithresh)

    labels = comp[1]
    labelStats = comp[2]
    labelAreas = labelStats[:, 4]

    for compLabel in range(1, comp[0], 1):

        if labelAreas[compLabel] > maxArea or labelAreas[compLabel] < minArea:
            labels[labels == compLabel] = 0

    labels[labels > 0] = 1

    # Do dilation
    se = cv.getStructuringElement(cv.MORPH_ELLIPSE, (25, 25))
    IdilateText = cv.morphologyEx(labels.astype(np.uint8), cv.MORPH_DILATE, se)

    # Find connected component again
    comp = cv.connectedComponentsWithStats(IdilateText)

    # Draw a rectangle around the text
    labels = comp[1]
    labelStats = comp[2]
    # labelAreas = labelStats[:,4]

    for compLabel in range(1, comp[0], 1):
        cv.rectangle(im, (labelStats[compLabel, 0], labelStats[compLabel, 1]), (
            labelStats[compLabel, 0] + labelStats[compLabel, 2], labelStats[compLabel, 1] + labelStats[compLabel, 3]),
                     (255, 255, 255), 2)

    im = im[labelStats[compLabel, 1]:labelStats[compLabel, 1] + labelStats[compLabel, 3],
        labelStats[compLabel, 0]:labelStats[compLabel, 0] + labelStats[compLabel, 2]]
    return im


def take_frame_out_of_image(frame):
    cropped_x1 = int(frame.shape[0] / 1.8)
    cropped_x2 = int(frame.shape[0] / 1.5 + frame.shape[0] / 8)
    cropped_y1 = 50
    cropped_y2 = int(frame.shape[1] - frame.shape[1] / 30)

    # cropping just a frame with brackets assigned for handwriting
    cropped_image_original = frame[cropped_x1:cropped_x2, cropped_y1:cropped_y2]

    # creating copy of image (problem with overwriting original one)
    cropped_image_black_white = cropped_image_original.copy()

    gray = cv.cvtColor(cropped_image_black_white, cv.COLOR_BGR2GRAY)

    ret, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY_INV)
    # setting white to black
    cropped_image_black_white[thresh == 255] = [255, 255, 255]
    # setting black to white - image before change
    cropped_image_black_white[thresh == 0] = 0

    # printing paper sheet in smaller size
    scale = 20
    widthscale = int(cropped_image_black_white.shape[1] * scale / 50)
    heightscale = int(cropped_image_black_white.shape[0] * scale / 50)

    dim = (widthscale, heightscale)

    cropped_image_frame_original = cv.resize(cropped_image_original, dim, interpolation=cv.INTER_AREA)
    resized_image_black_white = cv.resize(cropped_image_black_white, dim, interpolation=cv.INTER_AREA)
    # cv.imshow('cropped', resized_image_black_white)
    # cv.imshow('Resized black and white', resized_image_black_white)

    # taking coords from black_white picture to use them with origin one
    x, y, w, h = detect_frame_coordinates(resized_image_black_white)
    cropped_image_frame_original = cropped_image_frame_original[y:y + h, x:x + w]

    # cv.imshow('Cropped image frame original', cropped_image_frame_original)
    # recognize_word(cropped_image_frame_original)
    return cropped_image_frame_original
