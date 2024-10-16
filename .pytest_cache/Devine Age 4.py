CY = 2024  # current year
CM = 10    # current month
CD = 11    # current date

# Input for birth year, month, and date
year = int(input("Enter your year of birth here: "))

if year <= CY:  # check if the year given is valid
    # Leap year check
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        feb_days = 29  # Leap year
    else:
        feb_days = 28  # Non-leap year
    
    month = int(input("Enter your month of birth's number (1-12): "))
    
    if 1 <= month <= 12:  # check if the month is valid
        date = int(input("Enter your date of birth: "))
        
        # Validate the date based on the month
        if (month == 2 and date <= feb_days) or (month in [4, 6, 9, 11] and date <= 30) or (month in [1, 3, 5, 7, 8, 10, 12] and date <= 31):
            
            # Age calculation logic
            if year < CY:
                if month > CM or (month == CM and date > CD):
                    print("Your age is", CY - year - 1, "years old")
                else:
                    print("Your age is", CY - year, "years old")
            elif year == CY:
                if month < CM or (month == CM and date <= CD):
                    print("You are", CM - month, "months old")
                else:
                    print("You are", CM - month - 1, "months old")
        
        else:
            print("Please run the program again and enter a valid date.")
    
    else:
        print("Please run the program again and enter a valid month.")
else:
    print("Please run the program again and enter a valid year.")
