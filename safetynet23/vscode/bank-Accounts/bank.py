class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance=0):
        if name.lower() in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[name.lower()] = Account(name, initial_balance)
            print("Account created successfully.")

    def get_account(self, name):
        return self.accounts.get(name.lower())

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
        else:
            for account in self.accounts.values():
                print(f"Name: {account.name}, Balance: ${account.balance}")


def main():
    bank = Bank()

    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display All Accounts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter account holder name: ").strip()
            initial_balance = float(input("Enter initial balance (default 0): ") or 0)
            bank.create_account(name, initial_balance)
        elif choice == '2':
            name = input("Enter account holder name: ").strip()
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == '3':
            name = input("Enter account holder name: ").strip()
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == '4':
            name = input("Enter account holder name: ").strip()
            account = bank.get_account(name)
            if account:
                print(f"Current balance: ${account.get_balance()}")
            else:
                print("Account not found.")
        elif choice == '5':
            bank.display_all_accounts()
        elif choice == '6':
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()