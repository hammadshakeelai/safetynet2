keep_going = 'yes'
while keep_going == 'yes' or keep_going == 'y':
    sales =  float(input("Enter sales: "))
    commission_rate = float(input("Enter commission Rate: "))
    
    commission = sales * commission_rate
    print("Your Commission is", commission)
    keep_going =  input("To continue enter yes: ")
 
print("End")