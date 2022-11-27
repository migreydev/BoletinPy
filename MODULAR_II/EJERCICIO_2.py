'''
2. Design a method called isLeapYear that receives a number and returns False for
common years and True for leap years. You may know that a year is considered to
be a leap year if it is divisible by 4, unless it is also divisible by 100. A year is not a
leap year if it is divisible by 100 unless it is also divisible by 400.
'''
agno=int(input("Indique un año "))

def isLeapYear(agno):
    return agno%4==0 and (agno%100!=0 or agno%400==0)
print(isLeapYear(agno))
