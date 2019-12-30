import cv2 as cv
import numpy as np
from classes.handwriting_recognition import take_frame_out_of_image, recognize_word
import os
import os.path
from classes.csv_to_answers import return_questionaire_answers


def main():
    list_of_answers = return_questionaire_answers()
    get_handwriting_images_for_analysis(list_of_answers)
    imgray = cv.cvtColor(list_of_answers[0].NormalImage, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 220, 255, 0)

    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(list_of_answers[0].NormalImage, contours, -1, (0, 255, 0), 1)

    cv.waitKey(0)
    cv.destroyAllWindows()


def get_handwriting_images_for_analysis(list_of_answers):
    scanned_polls_path = 'images\\Scanned-polls'
    cropped_frame_path = 'images\\Cropped-frames-out-of-scanned-polls'

    # image_path takes already filled polls
    for i in os.listdir(scanned_polls_path):
        image_path = f'{scanned_polls_path}\\{i}'
        # print(f'Chosen path: {image_path}')
        try:
            file = open(image_path)
            file.close()
            image = cv.imread(image_path)
            normal = take_frame_out_of_image(image)
            cropped = recognize_word(take_frame_out_of_image(image))
            for j in list_of_answers:
                if i == (str(j.ID) + '.jpg'):
                    j.NormalImage = normal
                    j.CroppedImage = cropped
                    print(f'{i} Siadło')

        except FileNotFoundError:
            print(f'file {image_path} not found')
    counter = 0
    for j in list_of_answers:
        print(j.ID)
        if j.ID not in [23, 53, 74, 76, 88, 90, 135, 145]:
            if j.FeaturesList[0] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\CREATIVE\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[0] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\SCHEMATIC\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[1] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\SHY\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[1] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\CONFIDENT\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[2] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\ASSERTIVE\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[2] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\SUBMISSIVE\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[3] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\POSSESSED\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[3] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\EMOTIONAL\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[4] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\SPONTANOUS\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[4] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\RESERVED\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[5] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\PERFECT\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[5] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\MESSY\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[6] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\PERFECTIVE\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[6] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\UNPERFECTIVE\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[7] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\INTROVERT\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[7] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\EXTROVERT\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[8] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\ABSTRACT\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[8] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\CONSTANT\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[9] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\CONFORMING\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[9] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\NONCONFORMING\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[10] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\SUFFICIENT\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[10] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\DEPENDENT\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[11] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\EMOTIVE\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[11] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\EMOTIONLESS\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[12] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\OPTIMISTIC\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[12] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\PESSIMISTIC\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[13] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\PATIENT\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[13] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\IMPATIENT\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[14] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\SUSPICIOUS\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[14] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\TRUSTING\\{j.ID}.jpg",
                    j.NormalImage)

            if j.FeaturesList[15] < 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\ESTABLISHED\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.FeaturesList[15] >= 6:
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\NONESTABLISHED\\{j.ID}.jpg",
                    j.NormalImage)

            if j.Sex == 'Mężczyzna':
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\MEN\\{j.ID}.jpg",
                    j.NormalImage)
            elif j.Sex == 'Kobieta':
                cv.imwrite(
                    f"D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\images\\CNN\\WOMEN\\{j.ID}.jpg",
                    j.NormalImage)



if __name__ == '__main__':
    main()
