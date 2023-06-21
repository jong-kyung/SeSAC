import random
import calendar
import datetime

# 전역변수 설정
names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
genders = ['Male','Female']

# 각종 함수 설정
def generate_name():
    return random.choice(names)

def generate_birthdate():
    year = random.randint(1950, 2010) 
    month = random.randint(1,12)
    day = random.randint(1,calendar.monthrange(year, month)[1])
    age = datetime.date.today().year - year
    result = f"{year}-{month}-{day}"
    return result, age

def generate_gender():
    gender = random.choice(genders)
    return gender

def generate_address():
    street = random.randint(1,100)
    city = random.choice(cities)
    return f'{street, city}'

data = []
for _ in range(10):
    name = generate_name()
    birthdate = generate_birthdate()[0]
    gender = generate_gender()
    address = generate_address()
    data.append(name)

for d in data:
    print(d)