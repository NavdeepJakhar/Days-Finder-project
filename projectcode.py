# 'Days left till a date' Project

import datetime as dt
''' functionalities -
> find days from today's date
> find days from a particular date'''

# FROM date functions
def from_case1():
    funcdate=dt.date.today()
    return funcdate

def from_case2():
    fromyear=int(input("Enter year : "))
    frommonth=int(input("Enter month : "))
    fromdate=int(input("Enter date : "))
    funcdate=dt.date(fromyear,frommonth,fromdate)
    return funcdate


# TO date functions
def to_case1():
    toyear=int(input("Enter year : "))
    funcdate1=dt.date(toyear,1,1)
    return funcdate1

def to_case2():
    toyear=int(input("Enter year : "))
    tomonth=int(input("Enter month : "))
    todate=int(input("Enter date : "))
    funcdate1=dt.date(toyear,tomonth,todate)
    return funcdate1

# Subtraction function
def days_between(from_date,to_date):
    sub=to_date-from_date
    print("__________________________________________________________________________")
    print("------------------------------------------------------------------------\n")
    print("Days in between the dates =>",abs(sub))


# Driver Code
print("************************************************************************")
print("------------------------------------------------------------------------")
print("(Please read the readme file before using this to understand it better.)")
print("------------------------------------------------------------------------\n")
print("\t\t\t~ DAYS FINDER ~\n")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print("Number of days:")
print("FROM => 1. Today's date")
print("         2. Another date")
ch=int(input("\nYour choice [1/2] : "))
print("\n")
if ch==1:
    from_date=from_case1()
elif ch==2:
    from_date=from_case2()
else:
    print("Invalid choice.")
    quit()

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\n")
print("TO => 1. New Year date")
print("      2. A particular date")
ch1=int(input("\nYour choice [1/2] : "))
if ch1==1:
    to_date=to_case1()
elif ch1==2:
    to_date=to_case2()
else:
    print("\tInvalid choice.")
    quit()

days_between(from_date,to_date)
print("\n------------------------------------------------------------------------")
print("************************************************************************\n")