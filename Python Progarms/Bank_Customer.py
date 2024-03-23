class BankAccount:
    def __init__(self, acc_number):
        self.acc_number = str(acc_number)
        self.balance = float()
    

    def deposit(self, amount):
        self.balance += amount

    

    def withdraw(self, amount):
        if amount > self.balance:
            print('No enough balance')
        else:
            self.balance -= amount


    def get_balance(self):
        return self.balance
    

class Savings_Account(BankAccount):
    def __init__(self, acc_number, interest_rate):
        super().__init__(acc_number)
        self.interest_rate = interest_rate


    def add_interest(self):
        interest = self.balance * (self.interest_rate/100)
        self.balance += interest


class CheckingAccount(BankAccount):
    def __init__(self, acc_number, transaction_fee):
        super().__init__(acc_number)
        self.transaction_fee = transaction_fee

    
    def deduct_transaction_fee(self):
        self.balance -= self.transaction_fee

    
    def deposit(self, amount):
        self.deduct_transaction_fee()
        super().deposit(amount)
    

    def withdraw(self, amount):
        self.deduct_transaction_fee()
        super().withdraw(amount)



class Costumer:
    def __init__(self, name):
        self.name = name 
        self.accounts = []

    
    def add_account(self, account):
        self.accounts.append(account)


    def get_total_balance(self):
        total = float()
        for accounts in self.accounts:
            total += accounts.get_balance()
        
        print(f'The bank has {total}')




b = BankAccount(878778)
b.deposit(10000)
s = Savings_Account(8788778, 3.5)
n = CheckingAccount(87877880, 5)
co = Costumer('Ghazi')
co.add_account(b)
co.add_account(s)
co.add_account(n)
co.get_total_balance()


n.deposit(10000)
n.withdraw(10)
print(n.balance)




    


    