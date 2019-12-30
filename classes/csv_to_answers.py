import csv
from collections import Counter
import numpy as np


# Class which contains all answers from Google Form Questionnaire
class SinglePersonQuestionnaire:
    def __init__(self):
        self.FeaturesList = []

    def add_feature(self, value):
        self.FeaturesList.append(int(value))

    ID = 0
    FeaturesList = []
    AgeCategory = 0
    Sex = ''
    NormalImage = np.ndarray
    CroppedImage = np.ndarray


def return_questionaire_answers():
    # new_answers contain dicts of answers
    new_answers = [{}]
    with open('D:\\PROGRAMOWANIE\\Python programy\\OMR-handwriting-features-recognition\\formularz.csv', 'r',
              encoding='utf-8') as csv_file:
        answers = csv.DictReader(csv_file, delimiter=',', quotechar='"')
        for row in answers:
            new_answers.append(row)

    # list of all people's answers
    list_of_questionnaire = [SinglePersonQuestionnaire() for i in range(1, len(new_answers))]

    count = 1
    N = []
    # assigning answers to each person
    for questionnaire in list_of_questionnaire:
        questionnaire.ID = int(new_answers[count]['Identyfikator'])
        questionnaire.AgeCategory = new_answers[count]['Wiek']
        questionnaire.Sex = new_answers[count]['Plec']
        for i in range(1, 17):
            val = new_answers[count][f'{i}']
            questionnaire.add_feature(val)

        count += 1
        N.append(int(questionnaire.ID))
        # print(questionnaire.FeaturesList[13])

    N.sort()
    C = Counter(N)
    print(N)
    print([k, ] * v for k, v in C.items())

    return list_of_questionnaire
