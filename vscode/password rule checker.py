#15. Write a Python program to check the validity of passwords input by users.
#Validation :

#At least 1 letter between [a-z] and 1 letter between [A-Z].c4c5
#At least 1 number between [0-9].c3
#At least 1 character from [$#@].c2
#Minimum length 6 characters.c1
#Maximum length 16 characters.c1
password=str(input("enter an eligible password :  "))
length=len(password)
print(length)
c1=False
c2=False
c3=False
c4=False
c5=False
if 6<=length and length<=16:
    c1=True
for i in password:
    if i =="$" or i=="#" or i=="@":
        c2=True
    if i.isdigit():
        c3=True
    if i.isalpha():
        if i.islower():
            c4=True
        if i.isupper():
            c5=True
if c1==True and c2==True and c3 == True and c4==True and c5==True :
    print("password is eligible",c1,c2,c3,c4,c5)
else:
    print("password is not eligible",c1,c2,c3,c4,c5)