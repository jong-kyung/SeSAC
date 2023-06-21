# 계산기 객체 만들기
class Calculator:
    mode = None
    val1 = None
    val2 = None
    def calc(self): # 객체 내 함수의 첫번째 파라미터는 대부분 self를 넣어줌
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

    def input_mode(self):
        self.mode = input('연산모드를 입력하시오')
        operators = ['plus','minus','multiply','division','quit']
        if mode in operators:
            print('올바른 연산모드입니다.')
        else:
            print('알 수 없는 연산모드가 입력되었습니다. 가능한 연산자:', operators)
            mode = self.input_mode()

        return mode

    def input_value1(self):
        try:
            val1 = int(input('숫자1을 입력하시오'))
        except ValueError:
            print('올바른 숫자가 입력되지 않았습니다')
            print('다시 입력해주세요')
            val1 = self.input_value1()
        return val1

    def input_value2(self):
        try:
            val2 = int(input('숫자2을 입력하시오'))
        except ValueError:
            print('올바른 숫자가 입력되지 않았습니다')
            print('다시 입력해주세요')
            val2 = self.input_value2()
        return val2
    
    def operation(self):
        result = None

        if self.mode == 'plus':
            result = self.val1 + self.val2
        elif self.mode == 'minus':
            result = self.val1 - self.val2
        elif self.mode == 'multiply':
            result = self.val1*self.val2
        elif self.mode == 'division':
            try: 
                result = self.val1//self.val2
            except ZeroDivisionError:
                print('0으로 나눗셈을 할 수 없습니다.')
                result = 'NaN'
        
        else:
            print('알 수 없는 연산모드입니다.',self.mode)
        return result

calculator = Calculator()
calculator.operation()