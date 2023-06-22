numbers = [1,2,3,4,5]

value = numbers[1]

def get_number(index):
    try:
        # 오류 발생 가능성이 있는 코드 블럭
        return numbers[index]
    except IndexError:
        # 오류에 대한 처리 방법
        print('입력값에 대한 인덱스 번호가 잘못 되었습니다.')
    except TypeError:
        # 오류에 대한 처리 방법
        print('데이터 입력값의 유형이 잘못 되었습니다.')
    
    return None


# print(get_number(0))
# print(get_number(3))
# print(get_number('a'))
# print(get_number(-6))

# 미션1 
# 미션1-2 입력받은 글자를 숫자로 변환해서 +1 을 더해서 반환하시오 
# 미션2 사용자로부터 입력받아 해보시오

def convert_to_integer(param):
    value = None # 초기값을 설정해두는게 좋은 코드 초기값을 어떻게 설정할지 고민을 많이 해보아야 함

    try:
        value = int(param) + 1
    except ValueError:
        print ('변환할 수 없는 입력값입니다.')

    return value # return 되는 포인트를 try나 except안에 넣지 않는게 좋은 코드    

print(convert_to_integer('10'))
print(convert_to_integer('5'))
print(convert_to_integer('-5'))
print(convert_to_integer('A'))
print(convert_to_integer('Hello'))

user_input = input('>')
def convert_to_integer2():
    try:
        print(int(user_input)+1)
    except ValueError:
        print('데이터 value값이 잘못 되었습니다')
    
# convert_to_integer2()