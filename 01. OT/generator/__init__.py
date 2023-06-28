import csv
# 파이썬 스크립트를 실행과 함께 실행되는 파일
def load_file(filepath, param):
    with open(filepath) as file:
        OpenedFiles = file.readlines()
    for OpenedFile in OpenedFiles:
        param.append(OpenedFile.strip())

def write_file(filepath, param):
    with open(filepath, 'a', newline='\n') as file: 
                csv_file = csv.writer(file)
                csv_file.writerows(param)
                print('User 데이터 생성완료')