from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rect = Rectangle(5, 3)
print(rect.area())


# Task: Create a basic banking application with two types of accounts - SavingsAccount and CurrentAccount. Both
# account types should inherit from an abstract base class called BankAccount, which defines the common interface for
# bank accounts. Implement the deposit() and withdraw() methods in each account type.


class BankAccount(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount}to Savings Account {self.account_number}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} from Current Account {self.account_number}.")
        else:
            print("Invalid withdrawal amount.")


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} to Current Account {self.account_number}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} from Current Account {self.account_number}.")
        else:
            print("Invalid withdrawal amount.")


savings = SavingsAccount("SA0001")
current = CurrentAccount("CA0001")

savings.deposit(2000)
current.deposit(2000)
savings.withdraw(1000)
current.withdraw(1000)

print(savings.balance)
print(current.balance)
