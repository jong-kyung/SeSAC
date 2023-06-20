sentence='Hello world'

# 미션1. 원하는 글자 세기
# 미션2. 대소문자 구분하지 않고 글자 세기
def count_char(input_char):
    count = 0
    for char in sentence:
        if char.lower() == input_char.lower(): # upper() 혹은 lower()만 해도 동작이 가능함.
            count +=1
    return count

char = 'h'
count = count_char(char)
print(f'글자{char}갯수{count}')