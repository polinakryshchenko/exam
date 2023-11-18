class Transaction:
    def __init__(self, source_account, target_account, amount):
        self.source_account = source_account
        self.target_account = target_account
        self.amount = amount

    def execute(self):
        if 0 < self.amount <= self.source_account.balance:
            self.source_account.balance -= self.amount
            self.target_account.balance += self.amount
            print(f"Transaction of ${self.amount} from {self.source_account.owner}'s account to "
                  f"{self.target_account.owner}'s account completed.")
        else:
            print("Invalid transaction amount or insufficient funds.")


class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Added customer {customer.name} to the bank.")

class Account:
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def transfer(self, target_account, amount):
        transaction = Transaction(self, target_account, amount)
        transaction.execute()


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Added account #{account.account_number} to {self.name}'s accounts.")


# Створено банк та додано двох клієнтів і їх рахунки
bank = Bank()
customer1 = Customer("Sophia Lee")
customer2 = Customer("William Martinez")

account1 = Account(1, 1000, "Isabella Clark")
account2 = Account(2, 500, "William Martinez")
account3 = Account(3, 1500, "Sophia Lee")

customer1.add_account(account1)
customer1.add_account(account3)
customer2.add_account(account2)

bank.add_customer(customer1)
bank.add_customer(customer2)

# Виконано декілька операцій з рахунками та транзакції між ними
account1.deposit(200)
account1.withdraw(50)

account2.transfer(account1, 100)