# 미션1. 사용자로부터 문장을 입력받아 대문자로 변환하시오.
# 미션2. 입력받은 문장에서 대문자는 소문자로, 소문자는 대문자로 변환하시오
def convert_case(text):
    result = ''
    for i in text:
        if i.isupper():
            result += i.lower()
        elif i.islower():
            result += i.upper()
        else:
            result += i
    
    return result       

text= input('문자열을 입력하세요')
result = convert_case(text)
print('변환된 문장:',result)