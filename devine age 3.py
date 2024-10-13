CY=2024 #current year
CM=10 #current month
CD=11 #current date 
year=int(input("enter your year of birth here : "))
if year<=CY: #to check if number given is valid 
    month=int(input("enter your month of birth's number here(example: 2 for february) : "))
    if month<=12: #to check if number given is valid
        date=int(input("enter your date of birth here : "))
        if date<=31: #to check if number given is valid
            if year<CY:
                if month>=CM:
                    if month==CM:
                        if date<=CD:
                            print("your age is",CY-year,"years old")
                        else:
                            print("your age is",CY-year-1,"years old")
                    else:
                        print("your age is",CY-year-1,"years old")

                else:
                        print("your age is",CY-year,"years old")
            else:
                if date<=CD:
                    print("your age is ",CM-month,"months old")
                else:
                    print("your age is ",CM-month-1,"months old")       
        else:
            print("please run program again and enter correct month.")                
    else:
        print("please run program again and enter correct month.")
else:
    print("please run program again and enter correct year.")