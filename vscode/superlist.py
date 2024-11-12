h=11
for i in range (1,h+1):
    print(" "*(h-i),"*"*((2*i)-1),sep="")
for i in range (h,1,-1):
    print(' '*(h+1-i),"*"*((2*i)-3),sep="")