class Accaunt:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Owner of check: {self.owner}\nBalance : ${self.balance}'

    def deposite(self, dep_amt):
        self.balance += dep_amt
        print('You introduction is ready')

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Complete')
        else:
            print('no money no honey')


acct1 = Accaunt('Vlad', 100)

print(acct1.withdraw(120))
