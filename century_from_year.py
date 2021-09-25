
def century_from_year(year):
    return ( year // 100)+1
    return ( (year-1) // 100) + 1 

print(century_from_year(1989))    