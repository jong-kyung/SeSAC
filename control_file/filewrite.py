data = 'hello, world'

filepath = './data/'
filename = 'myfile.txt'

with open(filepath + filename,'w') as file: # w로 하면 이전 내용에 덮어씀
    file.write(data) 

print('파일 쓰기 완료!')