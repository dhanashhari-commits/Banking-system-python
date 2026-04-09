class Account:

    def __init__(self, account_number, customer_id, account_type, balance=0):
        self.account_number = account_number
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def check_balance(self):
        return self.balance

    def to_csv_row(self):
        return [self.account_number, self.customer_id, self.account_type, self.balance]
