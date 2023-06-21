# CSV : Comma Seperated Value
import csv

data = [
    ('name', 'age', 'city'),
    ('john', 25, 'seoul'),
    ('bill', 20, 'busan'),
    ('kim', 22, 'seoul'),
]
with open('user.csv', 'w', newline='\n') as file: # \n : newline, \r : linefeed
    csv_file = csv.writer(file)
    csv_file.writerows(data)

    print('csv write done')