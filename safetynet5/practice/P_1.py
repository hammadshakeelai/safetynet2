def R75():
    for i in range(1500,2701):
            if i%35==0:# % checks divisibilty
                print(i)
# R75()
def Celsius_and_Fahrenheit(input,output="celsius"):
    if output=="fahrenheit":
        return str(round(input*5/9+32,2))+"°F"
    elif output=="celsius":
        return str(round((input-32)/9*5,2))+"°C"
# print(Celsius_and_Fahrenheit(39))
def number_guess():
    import random
    guess=random.randint(1,9)
    number=0
    while number!=guess:
        number=int(input("enter your guess what the number is (1-9) : "))
    print("CORRECT")
# number_guess()
def sideways_pyramid():
    for i in range(1,6):
        for _ in range(i):
            print("*",end="")
        print("")
    for i in range(4,0,-1):
        for _ in range(1,i+1):
            print("*",end="")
        print("")
# sideways_pyramid()
def reverser(string):
    # word="hgjdk"
    # for char in range(len(word) - 1, -1, -1):
    # print(word[char], end="")
    output=""
    for char in string:
        output= char+output
    return output
# print(reverser("go nawaz"))
def evenodd_counter(numbers):
    even_counter=0
    odd_counter=0
    for i in numbers:
        if i%2==0:
            even_counter+=1
        else:
            odd_counter+=1
    return f"Number of even numbers : {even_counter} \nNumber of odd numbers : {odd_counter}"
# print(evenodd_counter([1,2,3,4,5,4,6,4,6,5,5,4,4,7,4,2]))
def print_class(datalist):
    for data in datalist:
        print(data,type(data))
# datalist = [1452, 11.23, 1+2j, True,'w3resource', (0, -1), [5, 12],{"class":'V', "section":'A'}]
# print_class(datalist)
def conntinue():
    for i in range(7):
        if i==3 or i==6:
            continue
        print(i,end=" ")
# conntinue()
def fibonacci():
    num1,num2=0,1
    for _ in range(9):
        num1,num2=num2,num2+num1
        print(num1)
# fibonacci()
def table(i,j):
    my_list=[]
    for k in range(i):
        my_list_inner=[]
        for _ in range(j):
            my_list_inner.append(_*k)
        my_list.append(my_list_inner)
    print(my_list)
# table(3,4)
def longdata():
    dataa=""" 


  GFT  


 """
    print(dataa.lower())
# longdata()
def fiveNoComma():
    string="0100,0011,1010,1001,1100,1001,0101,1111"
    binary4=""
    for char in string:
        if char==",":
            continue
        binary4=binary4+char
        if binary4== "1111" or binary4=="1010" or binary4=="0101":
            print(binary4)
        if len(binary4)==4:
            binary4=""
# fiveNoComma()
def lettersAndDigits():
    string="tg689.494.5TIGGG"
    listD="1234567890"
    numbers=0
    listA="abcdefghijklmnopqrstuvwxyz"
    letters=0
    for char in string:
        if char in listD:
            numbers+=1
        elif char.lower() in listA:
            letters+=1
    print("letters:",letters,"\nnumbers",numbers)
# lettersAndDigits()
def Validation():
    password=input("enter passoword: ")
    numbers,special,Uletters="1234567890","$#@","ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c1=c2=c3=c4=False
    Lletters=Uletters.lower()
    for _ in range(1):
        if 16>=len(password)>=6:
            for char in password:
                if char in numbers:
                    c1=True
                elif char in Uletters:
                    c2=True
                elif char in Lletters:
                    c3=True
                elif char in special:
                    c4=True
        if c1 and c2 and c3 and c4:
            print("valid")
        else:
            print("invalid")
# Validation()
def printo():
    for i in range(100,401):
        if i%2==0:
            print(i,end=",")
# printo()
def A():
    print(" ***\n*   *\n*   *\n*****\n*   *\n*   *\n*   *")
# A()
def D():
    print("****\n*   *\n*   *\n*   *\n*   *\n*   *\n**** ")
# D()
def E():
    print("*****\n*\n*\n****\n*\n*\n*****")
# E()
def G():
    print(" ***\n*   *\n*\n* ***\n*   *\n*   *\n ***")
# G()
def F():
    for _ in range(6):
        print("*")
    print("*****")
# F()
def M():
    for _ in range(7):
        print("*",end="")
        if _==2:
            print(" *   * ",end="")
        elif _==3:
            print("   *   ",end="")
        else:
            print("       ",end="")
        print("*")
# M()
def O():
    print(" ***\n*   *\n*   *\n*   *\n*   *\n*   *\n *** ")
# O()
def P():
    for _ in range(7):
        if _ ==0 or _==3:
            print("****")
        elif _==1 or _==2:
            print("*   *")
        else:
            print("*")
# P()
def R():
    counter=1
    for _ in range(7):
        if _ ==0 or _==3:
            print("****")
        elif _==1 or _==2:
            print("*   *")
        else:
            print("*"," "*counter,"*",sep="")
            counter+=1
# R()
def S():
    for _ in range(7):
        if _%3==0:
            print(" ***")
        elif _<3:
            print("*")
        else:
            print("    *")
# S()
def bigS():
    for i in range(15):
        if i<3 or 6<i<10 or 11<i<15:
            print("ooooooooooooooooo")
        elif i<10:
            print("oooooo")
        else:
            print("           oooooo")
# bigS()
def T():
    print("*********")
    for i in range(6):
        print("    *")
# T()
def U():
    for i in range(6):
        print("*   *")
    print(" ***")
# U()
def F():
    for i in range (7):
        if i==3:
            print("  *")
        elif i<2 or i>4:
            print("*   *")
        else:
            print(" * *")
# F()
def Z():
    print("*"*7)
    for i in range(5,0,-1):
        print(i*" ","*",sep="")
    print("*"*7)
# Z()
def countstar():
    n=9
    for i in range(1,n+1):
        print(i*str(i))
# countstar()
def mul_table():
    i=6
    for _ in range(1,11):
        print(i,"x",_,"=",_*i)
# mul_table()
def sum_n():
    n=112
    answer=0
    for i in range(n+1):
        answer+=i
    print("sum:",answer)
    print("average:",answer/n)
# sum_n()
def next_day():
    ymd = input("Enter the date (yyyy-mm-dd): ")
    year = int(ymd[0:4])
    month = int(ymd[5:7])
    day = int(ymd[8:10])
    d31 = [1, 3, 5, 7, 8, 10, 12]
    d30 = [4, 6, 9, 11]
    if month == 2 and day == 28 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
        day = 1
        month += 1
    elif month == 2 and day == 29:
        day = 1
        month += 1
    elif month in d30 and day == 30:
        day = 1
        month += 1
    elif month in d31 and day == 31:
        day = 1
        month += 1
        if month == 13:
            month = 1
            year += 1
    elif day < 28 or (month == 2 and day < 29):
        day += 1
    elif (month in d30 and day < 30) or (month in d31 and day < 31):
        day += 1
    print(f"{year:04d}-{month:02d}-{day:02d}")
# next_day()
def median():
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    num3=int(input("enter third number: "))
    print((num1+num2+num3)/3)
# median()
def Shengxiao(year):
    if year%12==4:
        print("rat")
    elif year%12==5:
        print("ox")
    elif year%12==6:
        print("tiger")
    elif year%12==7:
        print("rabbit")
    elif year%12==8:
        print("dragon")
    elif year%12==9:
        print("snake")
    elif year%12==10:
        print("horse")
    elif year%12==11:
        print("goat")
    elif year%12==0:
        print("monkey")
    elif year%12==1:
        print("rooster")
    elif year%12==2:
        print("dog")
    elif year%12==3:
        print("pig")
# Shengxiao(1973)
def seasons():
    season=int(input("month (1-12): "))
    if 2>=season>=1:
        print("winters")
    elif season<7:
        print("spring")
    elif season<10:
        print("summers")
    elif season<12:
        print("autumn")
    else:
        print("winters")
# seasons()
def Q_triangle(s1,s2,s3):
    if s1==s2==s3:
        print("equilateral")
    elif s1==s2 or s2==s3 or s1==s3:
        print("isosceles")
    else:
        print("scalene")
# Q_triangle()
def int_checker(string):
    nums=["0","1","2","3","4","5","6","7","8","9"]
    flag=True
    for char in string:
        if char not in nums:
            flag=False
    if flag:
        print("The string is a integer")
    else:
        print("The string is not an integer")
# int_checker("9857486047")
def monthdays(monthName):
    thirtyday=["april","june","september","november"]
    if monthName=="feburary":
        print("28/29 days ")
    elif monthName in thirtyday:
        print("30 days")
    else:
        print("31 days")
# monthdays("june")
def vowel(letter):
    vowels="aeiou"
    if letter in vowels:
        print("vowel")
    else:
        print("consonant")
# vowel("p")
def dog_age():
    age=int(input("enter dog age in years: "))
    if age>2:
        answer=21+(age-2)*4
    else:
        answer=10.5*age
    print("age in dog years is ",answer)
# dog_age()