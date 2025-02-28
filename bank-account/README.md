Here is a **README** file for your **Bank Account System** project:

---

# Bank Account System

## Overview
A simple bank account system implemented using Object-Oriented Programming (OOP) concepts in Python. This system contains two classes: `BankAccount` and `SavingsAccount`. It allows users to deposit, withdraw, and manage their account balances, with the option to apply interest for savings accounts.

## Requirements

### 1. Base Class: `BankAccount`
- **Attributes**:
  - `owner`: Name of the account holder.
  - `balance`: The account balance (default value is 0).
  
- **Methods**:
  - `deposit(amount)`: Adds money to the account. Only positive values are allowed.
  - `withdraw(amount)`: Deducts money from the account. Cannot withdraw more than the available balance.
  - `get_balance()`: Returns the current balance of the account.

### 2. Derived Class: `SavingsAccount`
- **Inherits from**: `BankAccount`
  
- **Additional Attribute**:
  - `interest_rate`: The interest rate for the savings account (default value is 2%).
  
- **Additional Method**:
  - `apply_interest()`: Adds interest to the account balance based on the set interest rate.

### 3. Functional Requirements
- **Deposit and Withdrawal Validation**:
  - Ensure only positive amounts are deposited or withdrawn.
  - Prevent withdrawals that exceed the available balance.
  
- **Interest Calculation**:
  - Allow users to apply interest for `SavingsAccount` using the `apply_interest()` method.
  
- **Display Balance**:
  - The `get_balance()` method returns the balance along with the account holder’s name.

## Installation

1. Clone this repository or download the files.
2. Open the project folder in your preferred Python environment.
3. Run the `bank_account.py` file to test the functionality.

## Example Usage

```python
# Create a BankAccount instance
account1 = BankAccount("John Doe", 1000)
account1.deposit(500)
account1.withdraw(200)
print(account1.get_balance())

# Create a SavingsAccount instance
savings = SavingsAccount("Jane Doe", 2000, 0.05)
savings.apply_interest()
print(savings.get_balance())
```

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is open-source and available under the [MIT License](LICENSE).
