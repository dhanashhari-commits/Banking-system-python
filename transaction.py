class Transaction:

    def __init__(self, transaction_id, account_number, transaction_type, amount, date):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = float(amount)
        self.date = date

    def display_transaction(self):
        return f"{self.transaction_type} {self.amount} on {self.date}"

    def get_summary(self):
        return f"{self.transaction_type} of {self.amount}"

    def is_large_transaction(self):
        return self.amount > 10000

    def to_csv_row(self):
        return [self.transaction_id, self.account_number, self.transaction_type, self.amount, self.date]
