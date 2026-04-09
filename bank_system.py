from datetime import datetime
from customer import Customer
from account import Account
from transaction import Transaction
from file_handler import FileHandler


class BankSystem:

    def __init__(self):
        self.customers = {}
        self.accounts = {}
        self.transactions = []
