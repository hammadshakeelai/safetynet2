CY=2024 #current year
CM=10 #current month
CD=11 #current date 
# Input for birth year, month, and date
year=int(input("enter your year of birth here : "))
if year<=CY: #to check if number given is valid 
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        feb_days = 29  # Leap year
    else:
        feb_days = 28  # Non-leap year
    month=int(input("enter your month of birth's number here (1-12) : "))
    if 1<=month<=12: #to check if number given is valid
        date=int(input("enter your date of birth here : "))
        if (month == 2 and date <= feb_days) or (month in [4, 6, 9, 11] and date <= 30) or (month in [1, 3, 5, 7, 8, 10, 12] and date <= 31):
            #to check if number given is valid

            if year < CY:
                if month > CM or (month == CM and date > CD):
                    print("Your age is", CY - year - 1, "years old")
                else:
                    print("Your age is", CY - year, "years old")
            elif year==CY:
                if month < CM or (month == CM and date <= CD):
                    print("your age is ",CM-month,"months old")
                else:
                    print("your age is ",CM-month-1,"months old")       
        else:
            print("please run program again and enter correct month.")                
    else:
        print("please run program again and enter correct month.")
else:
    print("please run program again and enter correct year.")
    #if you face any difficulties understanding my code call on my cell
    #883339565399