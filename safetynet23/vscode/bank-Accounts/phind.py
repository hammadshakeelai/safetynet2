list_names = ['none', 'hammad', 'shakeel', 'aizaz', 'bob']
list_balances = [0, 2000, 300, 450, 10]

def make_acc(name, balance, list_names, list_balances):
    list_names.append(name)
    list_balances.append(balance)
    print('Account created')
    return list_balances, list_names

def acc_num(name, list_names):
    for i in range(len(list_names)):
        if name == list_names[i]:
            return i
    return 0

def accounts(account_number, list_balances):
    return list_balances[account_number]

def operations(op, balance1, account_number, list_balances):
    if op == 0:
        print(f"Balance: ${balance1}")
    elif op == 1:
        deposit=-1
        while deposit<0:
            deposit = int(input("Enter deposit amount: "))
        balance1 += deposit
        list_balances[account_number] = balance1
        print("Deposit successful")
    elif op == 2:
        withdraw=balance1+1
        while withdraw>balance1 or withdraw<0:
            withdraw = int(input("Enter withdrawal amount: "))
            if withdraw>balance1:
                print("Insuficient Balance")

        balance1 -= withdraw
        list_balances[account_number] = balance1
        print("Withdrawal successful")

def main(list_names, list_balances):
    while True:
        i = int(input('Press: 0 for checking in, 1 for making account, 2 to exit: '))
        if i == 0:
            name = input("Enter Name: ")
            account_number = acc_num(name, list_names)
            if account_number != 0:
                op = int(input("0 to check balance, 1 to deposit, 2 to withdraw: "))
                operations(op, list_balances[account_number], account_number, list_balances)
            else:
                print("Account not found")
        elif i == 1:
            name = input("Enter Name: ")
            balance = int(input("Enter balance: "))
            list_balances, list_names = make_acc(name, balance, list_names, list_balances)
        elif i == 2:
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main(list_names, list_balances)