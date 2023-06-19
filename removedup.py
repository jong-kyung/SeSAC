data1 = [1, 2, 3, 4, 3, 2, 1, 5, 6, 7, 6, 5]

# 입력받은 값에서 중복을 제거하시오.
def remove_duplicate(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list: # num 이 unique_list에 없으면
            unique_list.append(num)
    return unique_list

unique_list = remove_duplicate(data1)

# 아래 내용을 한줄로 작성하시오.(파이썬 기능/함수를 최대한 사용해서)
def remove_duplicate2(numbers):
    return list(set(data1))

print('원본리스트:',data1)
print('유닉리스트:', unique_list)


