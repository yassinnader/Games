class Customer:
    def __init__(self, name, national_id, phone_number):
        self.name = name
        self.national_id = national_id
        self.phone_number = phone_number
        self.accounts = []

    def add_account(self, account):
        self.account.append(account)

class Account:
    def __init__(self, account_number, account_type, balance = 0.0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: + {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance -= amount
        self.transactions.append(f"Withdraw: - {amount}")
        return True
    
    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)
            self.transactions.append(f"Transferred: - {amount} to {other_account.account_number}")
            return True
        return False
    
    def show_transactions(self):
        print("Transaction History: ")
        for t in reversed(self.transacions[-10:]):
            print(t)

class BankSystem:
    def __init__(self):
        self.customers = {}

    def add_customers(self, name, national_id, phone):
        if national_id in self.customers:
            print("Customer already exists.")
        else:
            self.customers[national_id] = Customer(name, national_id, phone)
            print("Customer added.")

    def open_account(self, nationl_id, account_number, account_type, balance = 0):
        if nationl_id in self.customers:
            account = Account(account_number, account_number, balance)
            self.customers[nationl_id].add_account(account)
            print("Account opened.")
        else:
            print("Customer not found.")

    def get_customer_accounts(self, national_id):
        if national_id in self.customers:
            return 
            self.customers[national_id].accounts
        else:
            print("Customer not found.")
            return []
        
    