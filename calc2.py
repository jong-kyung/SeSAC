# 계산기 만들기
# 사용자로부터 입력을 받아서 계산을 한다 
# 연산모드를 입력받는다, 덧셈, 뺄셈, 곱셈 숫자를 여러개 입력 받고
# 숫자를 두개 입력 받는다.

# 실행 예시
# 연산 모드를 입력하시오. plus / minus / multiply / division
# 숫자 1을 입력하시오 : 
# 숫자 2를 입력하시오:

# 미션. 잘못된 입력값에 대한 예외 처리..
# 내 방식
class Calculator:
    def calc():
        try:
            user_input = input('연산 모드를 입력하시오')
            operators = ['plus','minus','multiply','division']
            result = None
            for operator in operators:
                if not operator == user_input:
                    result = '연산자를 올바르게 입력해주세요'
                    continue
                else:
                    val1 = int(input('숫자 1을 입력하시오'))
                    val2 = int(input('숫자 2를 입력하시오'))
                    if user_input == operators[0]:
                        result = val1 + val2
                    elif user_input == operators[1]:
                        result = val1 - val2
                    elif user_input == operators[2]:
                        result = val1*val2
                    elif user_input == operators[3]:
                        result = val1//val2
                    break
        except ValueError:
            print('숫자를 입력해주세요')
        return result

    # print(calc())

    # 방식2 
    # 미션3. 올바른 숫자가 입력 될때까지 재입력 함수로 입력값 처리

    # return을 안해줄거라면 mode = val1 = val2 = None 으로 전역에 셋팅해줌. 하지만 좋은 방법은 아님, 함수를 잘게 쪼갤수록 좋은 코드
    def input_mode():
        mode = input('연산모드를 입력하시오')
        operators = ['plus','minus','multiply','division','quit']
        if mode in operators:
            print('올바른 연산모드입니다.')
        else:
            print('알 수 없는 연산모드가 입력되었습니다. 가능한 연산자:', operators)
            mode = input_mode()

        return mode

    def input_value1():
        try:
            val1 = int(input('숫자1을 입력하시오'))
        except ValueError:
            print('올바른 숫자가 입력되지 않았습니다')
            print('다시 입력해주세요')
            val1 = input_value1()
        return val1

    def input_value2():
        try:
            val2 = int(input('숫자2을 입력하시오'))
        except ValueError:
            print('올바른 숫자가 입력되지 않았습니다')
            print('다시 입력해주세요')
            val2 = input_value2()
        return val2
    
    # mode = input_mode()
    # val1 = input_value1()
    # val2 = input_value2()

    # exit(1) # exit : 종류하는 함수, 파라미터: 종료코드임.
    def operation(mode, val1, val2):
        result = None

        if mode == 'plus':
            result = val1 + val2
        elif mode == 'minus':
            result = val1 - val2
        elif mode == 'multiply':
            result = val1*val2
        elif mode == 'division':
            try: # try catch 는 쓰여야 할 곳에만 쓰는게 좋음 (전체 코드를 감싸는게 아닌..)
                result = val1//val2
            except ZeroDivisionError:
                print('0으로 나눗셈을 할 수 없습니다.')
                result = 'NaN'
        
        else:
            print('알 수 없는 연산모드입니다.',mode)
        return result

    if __name__ == '__main__':
        # 모드가 quit 일때까지 계속 반복하기.
        mode = None
        while True:
            mode = input_mode()
            if(mode == 'quit'):
                break
            val1 = input_value1()
            val2 = input_value2()
            result = operation(mode,val1,val2)
            print('결과',result)
