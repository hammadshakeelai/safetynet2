num=95
str_=""
while num>0:
    digit=num%2
    num=num//2
    str_= str(digit) + str_
print(str_)
