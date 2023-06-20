import math

# 원의 넓이를 구하려고 한다면?
radius = 5
area = math.pow(radius,2)*math.pi

# 파이 알 제곱
print('원의 넓이:', area)

# 랜덤 넘버 생성

import random

# 하나의 주사위를 던졌을때
def roll_dice():
    dice_roll = random.randint(1,6)
    print(dice_roll)


# 주사위를 10번 던져서 나온 수
for i in range(0,10):
    roll_dice()

# 이 리스트를 무작위로 섞기
my_list =[1,2,3,4,5]
print('원본 리스트',my_list)
print('섞인 리스트',random.sample(my_list,len(my_list)))

# 다른방식1
random.shuffle(my_list)
print('섞인 리스트:', my_list)

# 다른방식2
def shuffle2():
    my_new_list = []

    list_len = len(my_list)

    for i in range(0,list_len):
        pick = random.randint(0,list_len - i - 1)
        my_new_list.append(my_list[pick])
        my_list.remove(my_list[pick])

    return my_new_list