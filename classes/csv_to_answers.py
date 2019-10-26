import csv


# here are my work code
class SinglePersonQuestionnaire:
    ID = 0
    featuresList = []
    ageCategory = 0
    sex = 0


new_answers = [{}]
with open('formularz.csv', 'r') as csv_file:
    answers = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    for row in answers:
        print(row['ID'])
        new_answers.append(row)

listOfQuestionnaires = [SinglePersonQuestionnaire() for i in range(len(new_answers))]

count = 1
for questionnaire in listOfQuestionnaires:
    questionnaire.ID = new_answers[count]['ID']
    questionnaire.ageCategory = new_answers[count]['Wiek']
    questionnaire.Sex = new_answers[count]['Płeć']
    count += 1
