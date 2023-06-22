data1 = [3, 7, 2, 9, 1, 4]
data2 = [33, 73, 23, 93, 13, 43]
data2 = [-33, -73, -23, -93, -13, -43]
data4 = []

# 입력받은 인자의 리스트 중에서 가장 큰 숫자를 반납하시오
def find_max(numbers):
    current_max = numbers[0]
    for num in numbers:
        if num > current_max : 
            current_max = num
            
    return current_max            

print('최대값:',find_max(data1))

# 사용자로부터 입력 받아서, (공백(스페이스))으로 구분된 문자열을 입력 받아서, max를 구하시오
def find_max2(text):
    numbers = []
    strings = text.split()
    for string in strings:
        numbers.append(int(string))

    return find_max(numbers)

user_input = input('숫자를 입력하시오(공백으로 구분):')
max_number = find_max2(user_input)
print(max_number)

# 리스트 컴프리헨션을 사용해서 위의 복잡한 과정을 1줄로 변경하시오
def find_max3(text):
    numbers = [int(string) for string in text.split()]
    return find_max(numbers)