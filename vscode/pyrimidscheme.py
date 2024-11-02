pyra=int(input("enter pyramid length :  "))
counter=1
space=""
for i in range(1,pyra+1):
    for j in range(i):
        if counter<10:
            space="  "
        else:
            space=" "
        print(counter,space,end="")
        counter+=1
    print("")