users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
]

# 이름을 입력 받아 사용자 정보(딕셔너리)를 반납하시오.
search_bob = {
    'name':'Bob',
    'age':30
} 

def find_users(search_user):
    result = []

    for user in users:
        if user['name'] == search_user['name'] and user['age'] == search_user['age']:
            result.append(user)

    return result

# result = find_users(search_bob)
# print(result)

''' find_users(search_user): 함수를 완성하시오.
search_user = { } 안에 있는 조건이 모두 매칭하는 사용자를 찾아내시오.
예). {"name" : "Bob" } 이 있으면 이름으로만 검색하고, {"name" : "Bob", "age" : 30} 이 있으면 이 두가지를 AND 로 비교해서 검색하고... 등 '''

def find_users2(param):
    result= []
    for user in users:
        for key, value in user.items():
            for key2, value2 in param.items():
                if key2 == key and value == value2:
                    result = user
    return result

result = find_users2(search_bob)
# print(result)

# 방식1
def find_users3(serach_user):
    result=[]

    for user in users:
        if (serach_user.get('name') is None or serach_user.get('name') == user.get('name') and serach_user.get('age') is None or serach_user.get('age') == user.get('age') and serach_user.get('location') is None or serach_user.get('location') == user.get('location')):
            result.append(user)

    return result

# 방식2
def matches_criteria(user,condition):
    for key, value in condition.items():
        if user.get(key) != value: # user 의 key 값과 value 값이 다르면 false반환
            return False
        
    return True

def find_users4(search_user):
    result = []
    for user in users:
        if matches_criteria(user,search_user):
            result.append(user)

    return result

find_users4(search_bob)

# 유닛테스트
search_bob1 = {
    'name':'Bob',
} # expect1

search_bob2 = {
    'age':30
} # expect1

search_bob3 = {
    'name':'Bob',
    'age':30
} # expect1

search_bob4 = {
    'name':'Bob',
    'age':31
} # expect0

search_bob5 = { } # expect3

# 미션1. 한줄 한줄 호출하면서 구현
def test_find_users():
    final_result = True

    if not (len(find_users4(search_bob1)) == 1):
        final_result = False
    if not (len(find_users4(search_bob2)) == 1):
        final_result = False
    if not (len(find_users4(search_bob3)) == 1):
        final_result = False
    if not (len(find_users4(search_bob4)) == 0):
        final_result = False
    if not (len(find_users4(search_bob5)) == 3):
        final_result = False

    if final_result is True:
        print('PASS')
    else:
        print('FAIL')


# test_find_users()

# 미션2 코드를 짧게 요약하기
test_cases = [search_bob1,search_bob2,search_bob3,search_bob4,search_bob5]
test_expect = [1,1,1,0,3]

def test_find_users2():
    final_result = True

    for i, test_case in enumerate(test_cases): # enumerate : 인덱tm 와 원소로 이루어진 튜플을 만들어줌
        if len(find_users4(test_case)) != test_expect[i]:
            final_result = False

    if final_result is True:
        print('PASS')
    else:
        print('FAIL')

test_find_users2()

# 미션3 효율적인 유닛테스트 만들기
test_cases2 = [
    {'case':search_bob1, 'expected_result':1},
    {'case':search_bob2, 'expected_result':1},
    {'case':search_bob3, 'expected_result':1},
    {'case':search_bob4, 'expected_result':0}, 
    {'case':search_bob5, 'expected_result':3} ]

def test_find_users3():
    final_result = True
    for case in test_cases2:
        if not len(find_users4(case['case'])) == case['expected_result']:
            final_result = False

    if final_result is True:
        print('PASS222')
    else:
        print('FAIL222')

test_find_users3()