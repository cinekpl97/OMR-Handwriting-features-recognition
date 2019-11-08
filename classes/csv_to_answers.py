import csv
from collections import Counter


# Class which contains all answers from Google Form Questionnaire
class SinglePersonQuestionnaire:
    def __init__(self):
        self.FeaturesList = []

    def add_feature(self, value):
        self.FeaturesList.append(value)

    ID = 0
    FeaturesList = []
    AgeCategory = 0
    Sex = ''


# new_answers contain dicts of answers
new_answers = [{}]
with open('..\\formularz.csv', 'r', encoding='utf-8') as csv_file:
    answers = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    for row in answers:
        new_answers.append(row)

# list of all people's answers
listOfQuestionnaires = [SinglePersonQuestionnaire() for i in range(1, len(new_answers))]

count = 1
N = []
# assigning answers to each person
for questionnaire in listOfQuestionnaires:
    questionnaire.ID = int(new_answers[count]['Identyfikator'])
    questionnaire.AgeCategory = new_answers[count]['Wiek']
    questionnaire.Sex = new_answers[count]['Plec']
    for i in range(1, 17):
        val = new_answers[count][f'{i}']
        questionnaire.add_feature(val)

    count += 1
    N.append(int(questionnaire.ID))

N.sort()
C = Counter(N)
print(N)
print([k, ] * v for k, v in C.items())
tmp = 0
list_of_same_values = []
for i in N:
    if (i == tmp) and (i not in list_of_same_values):
        list_of_same_values.append(i)
    tmp = i

print(list_of_same_values)
