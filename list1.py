# 1부터 10까지의 각 숫자의 제곱으로 이루어진 목록을 만들때 사용 하는 코드
sqaures = []
for x in range(1,11):
    sqaures.append(x**2)

# print(sqaures)

# 위 함수를 간결하게 표현
sqaures = [x**2] # 내가 원하는 것  정의하기

sqaures = [x**2 for x in range(1,11)] # 뒤에 내가 정의한 변수의 생성방식 작성하기

squares = [x**2 for x in range(1,11)]
# print(squares)

# 1부터 20까지의 짝수들로 리스트를 생성하시오
even_numbers = [x] # 내가 원하는 숫자를 표현할 정수
even_numbers = [x for x in range (1,21)]
even_numbers = [x for x in range (1,21) if x%2==0 ]
# print(even_numbers)

# 문자열의 각 글자를 순회하면서 대문자로 바꾸시오
word="hello"
upper_letters = [i.upper() for i in word ] # upper() : 대문자로 변경하는 메소드

# 문자열 길이가 3이하인 단어들만 선택하기
words = ['apple','banana','cherry','dragonfruit','egg']
short_words = [word for word in words if len(word) <=3]
print(short_words)