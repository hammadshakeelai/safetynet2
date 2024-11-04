pyra=int(input("enter pyramid length :  "))
counter=1
for i in range(1,pyra+1):
    for j in range(i):
        if 100>counter>=10:
            space="  "
        elif counter>=100:
            space=" "
        else:
            space="   "
        print(counter,space,end="")
        counter+=1
    print("")