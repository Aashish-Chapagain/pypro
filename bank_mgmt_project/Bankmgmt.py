import string
import secrets
import os
import json


RANDOM_VALUE = 11  


class Bank:

    customer_number = 0

    def __init__(self):
        self.customers = {}
        self.file_name = "customer.json"

        try:

            if os.path.exists(self.file_name):
                with open(self.file_name, "r") as file:
                    self.customers = json.load(file)
        except json.JSONDecodeError:
            self.customer_number = {}

    # creating the method for every new customer
    def create_new_account(self, name, balance, account_number, number):
        self.number = number
        self.name = name
        self.balance = balance
        self.account_number = account_number

        self.customers[name] = {"number":number, "account_number": account_number, "balance": balance}

    def save_to_json(self):
        with open(self.file_name, "w") as file:
            json.dump(self.customers, file, indent=4)

    def deposit(self):
        deposit_amount = int(input("enter deposit amount"))
        self.balance += deposit_amount

    def withdraw(self, amount):
        if amount <= self.balance:
            print(f"{amount} is debited from the account")
            self.balance -= amount
            self.save_to_json()
        else:
            print("Not enough balance! ")

    def display(self):
        print(self.name, self.balance, self.account_number)





bank = Bank()

def navigation():
    print("""create , deposit or withdraw money""")

def withdarw():
    amount = int(input("input enter the amount you want to withdraw"))
    bank.withdraw(amount)


withdarw()

name = input("enter name: ")

amount = int(input("Enter the first depoit: "))
account = "".join(
    secrets.choice(
        string.digits,
    )
    for _ in range(RANDOM_VALUE)
)
person = bank

person.create_new_account(name, amount, account)

person.save_to_json()


a = input("from deposit enter deposit : ")

if a == "despost":
    person.deposit()
