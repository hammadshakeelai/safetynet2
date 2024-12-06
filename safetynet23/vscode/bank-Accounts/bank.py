list_names=['none','hammad','shakeel','aizaz','bob']
list_balances=[0,2000,300,450,10]

def make_acc(name,balance,list_names,list_balances):
    list_names.append(name)
    list_balances.append(balance)
    print('account created')
    return list_balances,list_names

def acc_num(name,list_names):
    for i in range(len(list_names)):
        if name==list[i]:
            return i
    return 0

def accounts(account_number,list_balances):
    return list_balances[account_number]

def main():
    input=int(input('Press: 0 for making account, 1 for checking in'))
    if input==0:
        name=input("Enter Name:  ")
        balance=int(input("Enter balance:  "))
        make_acc(name,balance,list_names,list_balances)
    elif input==1:
        name=input("Enter Name:  ")
        if name=="":
            account_number=int(input(""))
            balance=accounts(account_number,list_balances)
            print("0 to check balance, 1 to deposit, 2 to withdraw")
        else:
            balance=accounts(acc_num(name,list_names),list_balances)
            print("0 to check balance, 1 to deposit, 2 to withdraw")