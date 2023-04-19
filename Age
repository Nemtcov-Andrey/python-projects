# Программа позволяет получить возраст от сегодняшней даты и даты рождения.

from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
print('Возраст от сегодняшней даты и даты рождения:', calculate_age(date(2012, 12, 14)), 'лет (год)')

