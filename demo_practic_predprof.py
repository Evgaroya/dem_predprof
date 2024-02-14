import csv

with open('grants.csv', encoding = 'CP1251') as file: #открываем файл, в качестве кодировки указваем CP1251
    reader = csv.reader(file, delimiter = ';', quotechar = '"') #пишем уазательна на чтение файла, указваем разделителем ";" 
    person_list = list(reader)[1:] #переводим файл в список и берем срез с 1-ой строки, т.к она отведена под названеи столбцов
    for id, full_name, project_id, nomination, prize in person_list: #перебираем параметры по котрорым будем осуществлять поиск
        if 'Ершова Агафья' in full_name: #если находим нужного нам человека, то выводим его результат согласно формату из задания
            print(f'Вы получили {prize} рублей в конкурсе {nomination} с номером заявки {project_id}')
            break

    sum_prize, count_nomination = {}, {}
    for 