# with open('names.txt','r') as file: # 파일을 열때 사용 되는 문법
# # 파일 열기 r = read, w = write, a = append
#     names = file.read() # 파일 읽어오기
#     print(names)

with open('names.txt','r') as file: # 파일을 열때 사용 되는 문법
# 파일 열기 r = read, w = write, a = append
    lines = file.readlines() # 파일 내용 한줄씩 읽어오기 : lines 에 담겨있음

names = []

for line in lines:
    names.append(print(line.strip())) # strip() : 공백제거


