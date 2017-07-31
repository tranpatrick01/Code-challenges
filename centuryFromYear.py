def centuryFromYear(year):
    if year % 100 == 0:
        century = year / 100
        return century
    else:
        century = year / 100
        century = int(century) + 1
        return century
 
    