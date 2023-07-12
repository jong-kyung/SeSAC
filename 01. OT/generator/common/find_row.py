import csv

def find_row(FileName, FindOne):
    find_datas = []
    with open(f'./csv/{FileName}s.csv', 'r', newline='') as file:
        csv_file = csv.DictReader(file)
        for data in csv_file:
           find_datas.append(data[FindOne]) 
    return find_datas