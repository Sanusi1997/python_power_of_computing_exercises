def is_leap_year(year):
    if year in range(1900, (10 ** 5) + 1):
        leap = False
        if year % 4 == 0 and year % 400 != 0 and year % 100 != 0:
            return True
        elif year % 100 == 0 and year % 4 == 0 and year % 400 == 0:
            return True
        else:
            return leap
    else:
        pass

if __name__ == '__main__':
    print(is_leap_year(2020))
