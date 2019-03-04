year = int(input("Enter a year A.D.: "))
leap_check = bool(year%4)
if leap_check == False:
    print(str(year), 'is a leap year')
if leap_check == True:
    print(str(year), 'is not a leap year')
