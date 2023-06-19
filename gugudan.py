# 구구단 함수 생성
def gugudan(): 
    for i in range (1,10):
        print(f'{i}단')
        for j in range(1,10):
            print(f'{i}x{j}={i*j}')

gugudan()