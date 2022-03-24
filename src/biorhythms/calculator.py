from math import sin, pi


def rhythms_on_day(i):
    return [sin(2*pi*i/j) for j in [23, 28, 33]]


def rhythm_data(birth_date, start_date, how_many_days=40):
    days_since_birth = (start_date-birth_date).days
    return [rhythms_on_day(i + days_since_birth) for i in range(how_many_days)]

