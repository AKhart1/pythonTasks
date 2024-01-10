
class BankAccount:
    total_account = 0
    def __init__(self, account_holder, initial_balance = 0):
        self.account_number = BankAccount.total_account
        self.account_holder = account_holder
        self.balance = initial_balance
        BankAccount.total_account += 1

    def deposit(self, amount):
        return self.balance + amount
        print(f'Deposited {amount} into account {self.account_holder}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Withdrawn {amount} from account {self}')
        else:
            print('Not enough')

    def get_balance(self):
        return f'Account {self.account_number} balance: {self.balance}'

    @classmethod
    def display_accounts(cls):
        print(f'Total accounts: {BankAccount.total_account}')

class SavingsAccount(BankAccount):
    rate = 0.09

    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance)
        self.account_type = 'Saving Account'

    def getInterestRate(self):
        interest = self.balance * self.rate
        self.balance += interest
        print(f'Interest: {self.account_number}')

class CheckingAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0, limit=100):
        super().__init__(account_holder, initial_balance)
        self.account_type = 'Checking Account'
        self.limit = limit

    def withdraw(self, amount):
        if self.balance + self.limit >= amount:
            self.balance -= amount
            print(f'Withdrawn {amount} from account {self.account_holder}')
        else:
            print('Exceeds overdraft limit')

if __name__ == '__main__':
    savings_account = SavingsAccount('Adam',1300)
    savings_account.deposit(500)
    savings_account.getInterestRate()
    print(savings_account.get_balance())

    checking_account = CheckingAccount('Ann', 6600, 300)
    checking_account.deposit(450)
    checking_account.withdraw(700)
    print(checking_account.get_balance())

    BankAccount.display_accounts()
