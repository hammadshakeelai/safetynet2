def n_fizzbuzz(n):
    for i in range(1,n+1):
        if i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        elif i%15==0:
            print("fizzbuzz")
        else:
            print(i)
#n_fizzbuzz(9)
def palindrome(c):
    b=c[::-1]
    if b==c:
        return "is palindrome"
    else:
        return "not palindrome"
#print(palindrome("fxgdhgy999999ynbhvyghdgxf"))
def calculator(num1,num2,operator):
    if operator=="/":
        num1/=num2
    elif operator=="*":
        num1*=num2
    elif operator=="+":
        num1+=num2
    elif operator=="-": 
        num1-=num2
    return num1
#print(calculator(6,9,"+"))
def primefinder(p):
    flag=True
    if p ==0:
        ret= "not prime"
    elif p==1:
        ret= "not prime"
    else:
        for i in range(p-1,1,-1):
            if p%i==0:
                flag=False
                ret= "not prime"
                break
                
        if flag:
            ret="prime"
    return ret
#print(primefinder(17))
def unique_string(s):
    flag=True
    list=[]
    for i in s:
        if i not in list:
            list.append(i)
        else:
            print("not unique")
            flag=False
            break
            
    if flag:
        print("unique")
#unique_string("74_dth!")
def bank_operate():
    balance=100
    while True:
        operation=4
        while 0>operation or operation>3:
            operation=int(input(" Dial: 0 to withdraw, 1 to deposit, 2 to check balance, 3 to exit: "))
        if operation==0:
            withdraw =balance+1
            while withdraw>balance:
                withdraw=int(input("enter withdraw amount : "))
                if withdraw>balance:
                    print("error , insuficent balance")
                    
            balance-=withdraw
            print(f"you withdrawed {withdraw} amount and new balance is {balance}")
        elif operation ==1:
            deposit=int(input("enter deposit amount : "))
            balance+=deposit
            print(f"new balance {balance}")
        elif operation==2:
            print("your balance is ", balance)
        elif operation==3:
            print("bank program exitted")
            break
#bank_operate()
def answer_checker(n):
    power=0
    k=0
    while n>k:
        k=pow(2,power)
        if k!=0:
            power+=1
    if n==k:
        p=n-k
    else:
        k/=2
        p=n-k
    p*=2
    p+=1
    return int(p)
#print(answer_checker(9))
def tic_cross():
    def print_octothrope(one,two,three,four,five,six,seven,eight,nine):
        print("       *       *      ","\n","   ",one,"   *   ",two,"   *   ",three,"   ","\n","       *       *      ","\n","* * * * * * * * * * * *","\n","       *       *      ","\n","   ",four,"   *   ",five,"   *   ",six,"   ","\n","       *       *      ","\n","* * * * * * * * * * * *","\n","       *       *      ","\n","   ",seven,"   *   ",eight,"   *   ",nine,"   ","\n","       *       *      ",sep="")
    def main():
        one = two = three = four = five = six = seven = eight = nine = " "
        l=[1,2,3,4,5,6,7,8,9]
        print("1 | 2 | 3","---------","4 | 5 | 6","---------","7 | 8 | 9",sep="\n")
        list=[]
        for i  in range(9):
            turn=0
            if i%2==0:
                symbol="x"
                j=1
            else:
                symbol="o"
                j=2
            while turn<1 or turn>9:
                while turn<1 or turn>9 or turn not in l:
                    turn=float(input(f"user{j}: enter which cell do you want to mark ; "))
                turn=int(turn)
                if turn in list:
                    turn=0
                else:
                    list.append(turn)
            if turn==1:
                one=symbol
            elif turn==2:
                two=symbol
            elif turn==3:
                three=symbol
            elif turn==4:
                four=symbol
            elif turn==5:
                five=symbol
            elif turn==6:
                six=symbol
            elif turn==7:
                seven=symbol
            elif turn==8:
                eight=symbol
            elif turn==9:
                nine=symbol
                
            print_octothrope(one,two,three,four,five,six,seven,eight,nine)
            if one=="x" and two=="x" and three=="x" or four=="x" and five=="x" and six=="x" or seven=="x" and eight=="x" and nine=="x" or one=="x" and four=="x" and seven=="x" or two=="x" and five=="x" and eight=="x" or three=="x" and six=="x" and nine=="x" or one=="x" and five=="x" and nine=="x" or three=="x" and five=="x" and seven=="x":
                print("user1 won")
                win="yes"
                break
            elif one=="o" and two=="o" and three=="o" or four=="o" and five=="o" and six=="o" or seven=="o" and eight=="o" and nine=="o" or one=="o" and four=="o" and seven=="o" or two=="o" and five=="o" and eight=="o" or three=="o" and six=="o" and nine=="o" or one=="o" and five=="o" and nine=="o" or three=="o" and five=="o" and seven=="o":
                print("user2 won")
                win="yes"
                break 
            else:
                win="no"
        if win!="yes":
            print("DRAW")
        
    while True:       
        main()
#tic_cross()
def time():
    from datetime import datetime
    n=datetime.now()
    return n
#print(time())
def auto_tic_cross():
    def print_octothrope(one,two,three,four,five,six,seven,eight,nine):
        print("       *       *      ","\n","   ",one,"   *   ",two,"   *   ",three,"   ","\n","       *       *      ","\n","* * * * * * * * * * * *","\n","       *       *      ","\n","   ",four,"   *   ",five,"   *   ",six,"   ","\n","       *       *      ","\n","* * * * * * * * * * * *","\n","       *       *      ","\n","   ",seven,"   *   ",eight,"   *   ",nine,"   ","\n","       *       *      ",sep="")
    def main():
        one = two = three = four = five = six = seven = eight = nine = " "
        l=[1,2,3,4,5,6,7,8,9]
        won=0
        lost=0
        print("1 | 2 | 3","---------","4 | 5 | 6","---------","7 | 8 | 9",sep="\n")
        list=[]
        flag=True
        import random
        for i  in range(9):
            turn=0
            while turn<1 or turn>9:
                while turn<1 or turn>9 or turn not in l:
                    if flag:
                        symbol="x"
                        turn=int(input("user: enter which cell do you want to mark ; "))
                    else:
                        symbol="o"
                        turn=random.choice(l)
                if turn in list:
                    turn=0
                else:
                    list.append(turn)
            if turn==1:
                one=symbol
            elif turn==2:
                two=symbol
            elif turn==3:
                three=symbol
            elif turn==4:
                four=symbol
            elif turn==5:
                five=symbol
            elif turn==6:
                six=symbol
            elif turn==7:
                seven=symbol
            elif turn==8:
                eight=symbol
            elif turn==9:
                nine=symbol
            flag= not flag
            print("")
            print_octothrope(one,two,three,four,five,six,seven,eight,nine)
            if one=="x" and two=="x" and three=="x" or four=="x" and five=="x" and six=="x" or seven=="x" and eight=="x" and nine=="x" or one=="x" and four=="x" and seven=="x" or two=="x" and five=="x" and eight=="x" or three=="x" and six=="x" and nine=="x" or one=="x" and five=="x" and nine=="x" or three=="x" and five=="x" and seven=="x":
                print("user won")
                win="yes"
                break
            elif one=="o" and two=="o" and three=="o" or four=="o" and five=="o" and six=="o" or seven=="o" and eight=="o" and nine=="o" or one=="o" and four=="o" and seven=="o" or two=="o" and five=="o" and eight=="o" or three=="o" and six=="o" and nine=="o" or one=="o" and five=="o" and nine=="o" or three=="o" and five=="o" and seven=="o":
                print("computer won")
                win="yes"
                break 
            else:
                win="no"
        if win=="no":
            print("DRAW")
    while True:       
        main()
#auto_tic_cross()
def josephus_problem(n_number_of_people):
    list=[]
    for i in range(1,n_number_of_people+1):
        list.append(i)
    flag=True
    while len(list)>1:
        tem_list=[]
        for i in list:
            if flag:
                tem_list.append(i)
            flag=not flag
        list=tem_list
    return list[0]
#print(josephus_problem(66))
def num_to_binary(num):
    binary=''
    list=[]
    while num>0:
        digit=num%2
        num=num//2
        list.insert(0,digit)
    for i in list:
        binary=binary+str(i)
    return binary
#print(num_to_binary(95))
def missing_num(num_list):
    size=len(num_list)
    for i in range(size+1):
        if i not in num_list:
            return i
# i=[0,9,8,7,6,5,4,1,2,3]
# print(missing_num(i))
def recursion_factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * recursion_factorial(n-1)
# print(recursion_factorial(5))
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1): a, b = b, a + b
    return a #if n > 0 else 0
# print(fibonacci(10))