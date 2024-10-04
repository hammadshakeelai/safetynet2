month=int(input("enter your month of birth's number here(example: 2 for february) : "))
date=int(input("enter your date of birth here : "))
year=int(input("enter your year of birth here : "))
CURRENT_YEAR=2024
CURRENT_MONTH=10
CURRENT_DATE=5
eventhappened1= month<=CURRENT_MONTH 
eventhappened2= date<=CURRENT_DATE


if eventhappened1==True and eventhappened2==True:
    age=CURRENT_YEAR-year
    print( "your age is : ",age)
else:
    age2=CURRENT_YEAR-year-1
    print("your age is : ",age2)