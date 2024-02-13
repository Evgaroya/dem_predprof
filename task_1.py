'''
Все ребята сдали свои проекты и получили оценки на защите, но Хадаров Владимир все прослушал
и просит помочь ему узнать какую оценку за проект он получил. Пожалуйста, подскажите
Владимиру какую оценку он получил. Формат вывода: Ты получил: <ОЦЕНКА>, за проект - <id>
Пока помогали Владимиру увидели, что многие ученики потеряли свои оценки при выкачке с
сайта. Из-за этого нет возможности посмотреть общую статистику. Чтобы избежать путаницы
поставьте вместо ошибки среднее значение по классу и округлите до трех знаков после запятой.
Сохраните данные в новую таблицу с названием student_new.csv.
'''

import csv

with open('students.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    student_list = list(reader)[1:]
    for id, name, title_project_id, class_stud, score in student_list:

        if 'Мельников Дмитрий' in name:
            print(f'Ты получил: {score}, за проект - {title_project_id}')
            break
    sum_class, count_class = {}, {} # dict()
    for student in student_list:
        print(student)
        if student[-2] in count_class:
            count_class[student[-2]] += 1
        else:
            count_class[student[-2]] = 1
        sum_class[student[-2]] = sum_class.get(student[-2], 0) + (int(student[-1]) if student[-1] != 'None' else 0)
    for student in student_list:
        if student[-1] == 'None':
            student[-1] = round(sum_class[student[-2]] / count_class[student[-2]], 3)

'''   
with open('student_new.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writerows(student_list)'''
    