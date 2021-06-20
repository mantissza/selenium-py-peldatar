# 037.md hw's solution aka leap year with function

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


print("Enter a year: (YYYY format) ")
user_input = int(input())
if leap_year(user_input):
    print("%i is a leap year." % user_input)
else:
    print("%i isn't a leap year." % user_input)
