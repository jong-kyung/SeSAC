import random
import calendar
import datetime

class BirthdateGenerator:
    def generate_birthdate(self):
        year = random.randint(1950, 2010) 
        month = random.randint(1,12)
        day = random.randint(1,calendar.monthrange(year, month)[1])
        age = datetime.date.today().year - year
        result = f"{year}-{month}-{day}"
        return result, age
