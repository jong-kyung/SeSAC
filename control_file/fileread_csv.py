import csv

with open('user.csv', 'r') as file: # \n : newline, \r : linefeed
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)