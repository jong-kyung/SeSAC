import csv

def SaveToCSV(FileName, Chart):
    with open(f'./chart_list/{FileName}.csv', 'w', newline='') as file:
        csv_data = csv.DictWriter(file, fieldnames= ['Title', 'Artist', 'AlbumTitle'])
        csv_data.writeheader()
        csv_data.writerows(Chart)