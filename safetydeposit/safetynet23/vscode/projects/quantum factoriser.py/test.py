my_list=[]
# import random
my_list_ofN=[ 15, 21, 33, 35, 55, 77]
# N=int(input('enter the N number: '))
# N=55
for N in my_list_ofN:
    print(f'number to get factorised: {N}')
    #N=P*Q
    G=8

    power=1

    while True:
        # print(power)#-----------------------
        if (G**power)%N==1:
            break
        power+=1
    # print(power)#-----------------------

    #((G**power/2)+1)((G**power/2)-1)== mN
    # ( P *f1) * ( Q *f2) == mN
    my_list.append((G**(power/2))+1)
    # print(((G**power/2)+1))#------------------
    my_list.append((G**(power/2))-1)
    # print((G**power/2)-1)#----------------------
    #euclids algorithm
    for numerator in my_list:
        divisor=N
        while True:
            
            remainder=numerator%divisor
            if numerator%divisor == 0:
                print(f'factor : {divisor}')
                break
            numerator=divisor
            divisor=remainder
    
    
    