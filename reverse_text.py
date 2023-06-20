def palindrome(str):
    reversed_str = str[::-1]
    if str.lower().replace(' ','') == reversed_str.lower().replace(' ',''):
        return True
    
    return False

print(palindrome('A n n a'))