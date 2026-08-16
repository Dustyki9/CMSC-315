"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class BankAccount:
    bank_name = "First National Bank"  # class variable - shared by all accounts

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # instance variable
        self.balance = balance                # instance variable

    def description(self):
        return f"{self.account_holder}'s account at {self.bank_name} has a balance of ${self.balance}."


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class SavingsAccount(BankAccount):
    interest_rate = 0.02  # new class variable - 2% interest, shared by all savings accounts

    def __init__(self, account_holder, balance, account_number, min_balance):
        super().__init__(account_holder, balance)  # reuse BankAccount's constructor
        self.account_number = account_number  # new instance variable
        self.min_balance = min_balance        # new instance variable

    def apply_interest(self):  # new method
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        return f"Interest applied: ${interest_earned:.2f}. New balance: ${self.balance:.2f}"

    def description(self):  # overrides BankAccount's description method
        return (f"Savings Account #{self.account_number} for {self.account_holder}: "
                f"${self.balance:.2f} at {self.interest_rate * 100:.0f}% interest, "
                f"min balance ${self.min_balance}.")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    acct1 = SavingsAccount("Alex Rivera", 1000, "SA-1001", 100)
    acct2 = SavingsAccount("Jordan Lee", 2500, "SA-1002", 500)

    print("Class access:", SavingsAccount.interest_rate)   # accessed via the class
    print("Instance access:", acct1.interest_rate)         # accessed via an object

    acct1.overdraft_protection = True  # new attribute added to acct1 only

    print("acct1 namespace:", acct1.__dict__)   # only acct1's own attributes
    print("acct2 namespace:", acct2.__dict__)   # acct2 never got overdraft_protection
    print("Class namespace:", SavingsAccount.__dict__)  # shared class-level namespace


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    acct1 = SavingsAccount("Alex Rivera", 1000, "SA-1001", 100)
    acct1.transaction_history = ["deposit $100", "deposit $50"]  # nested mutable data (list)

    shallow = copy(acct1)     # shallow copy - new object, but shares the SAME transaction_history list
    deep = deepcopy(acct1)    # deep copy - new object with its OWN independent transaction_history list

    acct1.transaction_history.append("withdrawal $30")  # mutate the original's nested list

    # Shallow copy shares the same nested list as the original,
    # so mutating acct1.transaction_history also changes shallow.transaction_history.
    # Deep copy creates a completely separate list,
    # so acct1.transaction_history changes do NOT affect deep.transaction_history.

    print("Original transaction history:", acct1.transaction_history)
    print("Shallow copy transaction history:", shallow.transaction_history)  # includes withdrawal - same list object
    print("Deep copy transaction history:", deep.transaction_history)         # does NOT include withdrawal - independent list


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    my_account = BankAccount("Sam Carter", 750)
    print("my_account.description(): ", my_account.description())

    my_savings = SavingsAccount("Alex Rivera", 1000, "SA-1001", 100)
    print(my_savings.description())
    print(my_savings.apply_interest())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()