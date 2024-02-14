import csv

with open('grants.csv', encoding = 'CP1251') as file: #открываем файл, в качестве кодировки указваем CP1251
    reader = csv.reader(file, delimiter = ';', quotechar = '"') #пишем уазательна на чтение файла, указваем разделителем ";" 
    person_list = list(reader)[1:] #переводим файл в список и берем срез с 1-ой строки, т.к она отведена под названеи столбцов
    for id, full_name, project_id, nomination, prize in person_list: #перебираем параметры по котрорым будем осуществлять поиск
        if 'Ершова Агафья' in full_name: #если находим нужного нам человека, то выводим его результат согласно формату из задания
            print(f'Вы получили {prize} рублей в конкурсе {nomination} с номером заявки {project_id}')
            break

    sum_nomination, count_nomination = {}, {}
    for person in person_list:
        print(person)
        if person[-2] in count_nomination:
            count_nomination[person[-2]] += 1
        else:
            count_nomination[person[-2]] = 1

        sum_nomination[person[-2]] = sum_nomination.get(person[-2], 0) + (int(person[-1]) if person[-1] != 'NULL' else 0)
    for person in person_list:
        if person[-1] == 'NULL':
            person[-1] = round(sum_nomination[person[-2]] / count_nomination[person[-2]], 3)

with open('person_new.csv', 'w', newline='', encoding='CP1251') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'Full_Name', 'project_id', 'nomination', 'prize'])
    writer.writerows(person_list)
