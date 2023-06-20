def palindrome(str):
    reversed_str = str[::-1] # 인덱싱에 ::-1 을하면 역순으로 복사됨
    if str.lower().replace(' ','') == reversed_str.lower().replace(' ',''):
        return True
    
    return False

print(palindrome('A n n a'))