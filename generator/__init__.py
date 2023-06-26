# 파이썬 스크립트를 실행과 함께 실행되는 파일

def load_file(filename):
    with open(filename) as file:
        first_names = file.readlines()