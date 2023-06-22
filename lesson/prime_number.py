def get_prime_number(number):
    result = []
    for num in range(2, number):
        if is_prime(num):
            result.append(num)
    
    return result

def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    
    return True

print(get_prime_number(30))