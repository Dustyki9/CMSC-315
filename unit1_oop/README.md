# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

For this assignment I built out a banking system to practice inheritance, namespaces, and copying in Python. I made a `BankAccount` parent class and a `SavingsAccount` child class that inherits from it.

## What I Did

### Parent Class: BankAccount

I started with `BankAccount` to represent a basic account. It has one class variable, `bank_name`, that's the same for every account no matter who owns it. Then I gave it two instance variables, `account_holder` and `balance`, set inside `__init__` so each account can hold its own info. I also wrote a `description()` method that returns a string with the account holder's name, balance, and bank name.

### Child Class: SavingsAccount

Next I made `SavingsAccount` inherit from `BankAccount`. It has its own class variable, `interest_rate`, set to 2% and shared across all savings accounts. I added two new instance variables, `account_number` and `min_balance`, in the constructor. Instead of rewriting the account_holder/balance logic again, I used `super().__init__()` to call `BankAccount`'s constructor and let it handle that part.

I also added a new method, `apply_interest()`, that calculates interest based on `interest_rate` and adds it to the balance. Then I overrode `description()` so `SavingsAccount` prints a more detailed summary that includes the account number, interest rate, and minimum balance. When I called `.description()` on a `SavingsAccount` object, it used my new version instead of the parent's — which is exactly what overriding is supposed to do.

### Namespace Demonstration

For `demonstrate_namespaces()`, I created two `SavingsAccount` objects. I accessed `interest_rate` both through the class (`SavingsAccount.interest_rate`) and through one of the instances (`acct1.interest_rate`) — both gave the same value, since the instance just looks it up on the class if it doesn't have its own copy.

Then I added a new attribute, `overdraft_protection`, to only one of the accounts after creating it. When I printed each object's `__dict__`, only `acct1` had `overdraft_protection` in it — `acct2` never saw it, since it only got added to `acct1` specifically. I also printed `SavingsAccount.__dict__` to show the class's own namespace, which had `interest_rate` and the method definitions, but none of the instance-only stuff.

### Copy Demonstration

For `demonstrate_copying()`, I created a `SavingsAccount` and gave it a `transaction_history` list as the nested mutable data. I made a shallow copy and a deep copy using `copy()` and `deepcopy()`. Then I appended a new transaction to the original's list.

After that, the shallow copy's `transaction_history` also showed the new transaction, but the deep copy's didn't. That's because a shallow copy only duplicates the outer object — anything nested, like a list, is just shared by reference, so the original and the shallow copy were literally pointing at the same list in memory. A deep copy actually rebuilds the nested list from scratch, so it stayed independent even after I changed the original.

### Main Function

In `main()`, I created one `BankAccount` and one `SavingsAccount`, called `.description()` on both to show inheritance and overriding in action, then called `demonstrate_namespaces()` and `demonstrate_copying()` to run both demos.

## Sample Output

```
=== Unit 1 OOP Assignment ===
my_account.description():  Sam Carter's account at First National Bank has a balance of $750.
Savings Account #SA-1001 for Alex Rivera: $1000.00 at 2% interest, min balance $100.
Interest applied: $20.00. New balance: $1020.00

=== Namespace Demonstration ===
Class access: 0.02
Instance access: 0.02
acct1 namespace: {'account_holder': 'Alex Rivera', 'balance': 1000, 'account_number': 'SA-1001', 'min_balance': 100, 'overdraft_protection': True}
acct2 namespace: {'account_holder': 'Jordan Lee', 'balance': 2500, 'account_number': 'SA-1002', 'min_balance': 500}
Class namespace: {'__module__': '__main__', 'interest_rate': 0.02, '__init__': <function SavingsAccount.__init__ at 0x...>, 'apply_interest': <function SavingsAccount.apply_interest at 0x...>, 'description': <function SavingsAccount.description at 0x...>, '__doc__': None}

=== Copy Demonstration ===
Original transaction history: ['deposit $100', 'deposit $50', 'withdrawal $30']
Shallow copy transaction history: ['deposit $100', 'deposit $50', 'withdrawal $30']
Deep copy transaction history: ['deposit $100', 'deposit $50']
```

## What I Took Away From This

- Inheritance let me reuse `BankAccount`'s logic in `SavingsAccount` without copy-pasting it, using `super()` to call the parent's constructor.
- Overriding showed me that Python checks the child class first when you call a method, so a subclass can straight up replace a parent's method just by reusing the name.
- Class variables are shared across every instance, but instance variables are private to whatever object they were set on — adding `overdraft_protection` to one account proved that.
- Shallow copies just copy references to nested data, so the original and the copy end up sharing the same list under the hood. Deep copies actually build a separate copy of everything nested, so they stay fully independent.
