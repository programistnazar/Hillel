# Прочитать сохранённый json-файл из задания №17 и записать данные
# на диск в csv-файл, первой строкой которого озаглавив каждый
# столбец и добавив новый столбец “телефон”.

import json
import csv

with open("task.json", 'r') as f:
    output_dict = json.load(f)


name_fields = ['Number', 'Name', 'Age', 'Phone']
phone = [1094345353, 342342, 43432, 343434, 4334]

with open('task_1.csv', 'w') as f:
    file_writer = csv.writer(f)
    counter = 0
    for key, value in (output_dict.items()):
        value.insert(0, key)
        value.insert(4, phone[counter])
        if counter == 0:
            file_writer.writerow(name_fields)
        counter += 1
        file_writer.writerow(value)
