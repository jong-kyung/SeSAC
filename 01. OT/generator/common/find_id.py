import csv

def find_id(FileName):
    id_datas = []
    with open('.csv/{FileName}s.csv', 'r', newline='') as file:
        csv_file = csv.reader(file)
        for data in csv_file:
            print(data)
