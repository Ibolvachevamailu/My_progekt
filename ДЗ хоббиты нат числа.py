def leap_year(year):
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('you shall pass')
    else:
        print('you shall not  pass')
  


leap_year('5')

