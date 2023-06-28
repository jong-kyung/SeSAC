# 튜플 (a,b)
def get_name_and_age():
    return 'john', 25


name, age = get_name_and_age()
print(name)
print(age)

# 리스트 - 배열 []형태로 관리
shopping_list = ["apple","banana","orange"]
print(shopping_list)
# 자료 추가
shopping_list.append('grape') 
print(shopping_list)
# 자료 삭제
shopping_list.remove('banana')
print(shopping_list)

# 딕셔너리(Dictionary) 활용
# key-value, "이름":"이종경"
student = {
    'name':'John',
    'age':29,
    'university':'ABC uni'
}

print("Name:",student['name'])
print("Age:",student['age'])

#---------------
numbers =[1,2,3,4,5]

for num in numbers:
    if num%2 == 0:
        print(num,"is 짝수")
    else:
        print(num,"is 홀수")

# 홀수 리스트와 짝수 리스트를 따로 만들어서, 목록에 추가하시오
even_numbers = []
odd_numbers = []
for num in numbers:
    if num%2 ==0:
        even_numbers.append(num)
    else :
        odd_numbers.append(num)
print(even_numbers, odd_numbers)

student_grades = {'John':85,'Emily':92,'Michael':78,'Sophia':95}
for student,grade in student_grades.items():
    if grade > 90:
        print(student)
        