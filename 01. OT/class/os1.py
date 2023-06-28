import os

current_dir = os.getcwd() # cwd <- current working directory
print('내 현재 폴더(디렉토리):',current_dir)

new_dir = 'sesac_1234'
# os.mkdir(new_dir) # mk <- make, dir <- directory

# 환경변수 접근
# python_path = os.getenv('PYTHONPATH') 
# print(python_path)

# os에 접근하여 명령할 수 있음
# my_commands = ['ls -l']
# for com in my_commands:
#     os.system(com)