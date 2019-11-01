import csv


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

# assigning answers to each person
for questionnaire in listOfQuestionnaires:
    questionnaire.ID = new_answers[count]['Identyfikator']
    questionnaire.AgeCategory = new_answers[count]['Wiek']
    questionnaire.Sex = new_answers[count]['Plec']
    for i in range(1, 17):
        val = new_answers[count][f'{i}']
        questionnaire.add_feature(val)

    count += 1

print(len(listOfQuestionnaires[3].FeaturesList))
