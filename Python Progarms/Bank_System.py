class BankAccount:
    def __init__(self, acc_number, holders_name):
        self.acc_number = acc_number
        self.acc_holders_name = holders_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount 

    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print('Not enoght amount')

    
    def get_balance(self):
        return self.balance
    

class Bank:
    def __init__(self):
        self.accounts = {}

    def get_account(self, acc_number):
        return self.accounts.get(acc_number, None)
    

    def create_account(self, acc_number, acc_holders_name):
        if acc_number not in self.accounts:
            new_account = BankAccount(acc_number,acc_holders_name)
            self.accounts[acc_number] = new_account
            print(f'The Account has been Created with the account number {acc_number} and the holders name is {acc_holders_name}')
        else:
            print('Account Already Created')

    
    def deposit(self, acc_number,amount):
        account = self.get_account(acc_number)
        if account:
            account.deposit(amount)
            print(f'Amount Successfully deposited in {acc_number}')
        else:
            print('No Account Found')


    def withdraw(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            account.withdraw(amount)
            print(f'Amount withdrwed Successfully from {acc_number}')
        else:
            print('No account Found')


    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        if from_account and to_account:
            from_account.withdraw(amount)
            to_account.deposit(amount)
        else:
            print('Account numbers were not accurate')

    

    def display_account_info(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(f"Account Number: {account.acc_number}")
            print(f"Account Holder: {account.acc_holders_name}")
            print(f"Balance: {account.get_balance()}")
        else:
            print("Account not found.")



    def calculate_total_balance(self):
        total_balance = sum(account.get_balance() for account in self.accounts.values())
        return total_balance



    



# Example usage:
bank = Bank()

bank.create_account("12345678", "John Doe")
bank.create_account("98765432", "Jane Smith")

bank.deposit("12345678", 1000)
bank.deposit("98765432", 500)

bank.transfer("12345678", "98765432", 1000000)






        