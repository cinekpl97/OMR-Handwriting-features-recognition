import csv


# here are my work code
class SinglePersonQuestionnaire:
    def __init__(self):
        self.FeaturesList = []

    def add_feature(self, value):
        self.FeaturesList.append(value)
    ID = 0
    FeaturesList = []
    AgeCategory = 0
    Sex = ''


new_answers = [{}]
with open('..\\formularz.csv', 'r', encoding='utf-8') as csv_file:
    answers = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    for row in answers:
        # print(row['Identyfikator'])
        new_answers.append(row)

listOfQuestionnaires = [SinglePersonQuestionnaire() for i in range(1, len(new_answers))]

count = 1
for questionnaire in listOfQuestionnaires:
    questionnaire.ID = new_answers[count]['Identyfikator']
    questionnaire.AgeCategory = new_answers[count]['Wiek']
    questionnaire.Sex = new_answers[count]['Plec']
    for i in range(1, 17):
        val = new_answers[count][f'{i}']
        questionnaire.add_feature(val)

    count += 1

print(len(listOfQuestionnaires[3].FeaturesList))
