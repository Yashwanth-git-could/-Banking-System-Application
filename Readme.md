# Banking System Application
This is a simple Banking System built using Python and MySQL, allowing users to register, login, deposit money, withdraw money, check their balance, and view their transaction history.

## Features

1. **User Registration**: Users can create a new account by providing a username and password.
2. **User Login**: Registered users can log in with their username and password.
3. **Check Balance**: Users can check their current account balance.
4. **Deposit Money**: Users can deposit money into their account.
5. **Withdraw Money**: Users can withdraw money from their account, provided they have sufficient balance.
6. **Transaction History**: Users can view a history of all their transactions (deposits and withdrawals), sorted by transaction date.

## Prerequisites

- Python 3.x
- MySQL Server
- MySQL Connector for Python (`mysql-connector-python`)

## Setup and Installation

### 1. Install MySQL

Install MySQL on your system and set up a database (e.g., `bankrecords`). Create the following tables in your MySQL database:

```sql
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    balance DECIMAL(10, 2) DEFAULT 0.00
);

CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    type VARCHAR(10),
    amount DECIMAL(10, 2),
    transaction_date DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

```
### 2. Install Python Dependencies

Install the MySQL Connector for Python by running the following command:

``` bash
pip install mysql-connector-python
``` 
### 3. Update Database Credentials
In the banking_system.py file, update the following connection details to match your MySQL setup:
```
mydb = mysql.connector.connect(
    user="root",
    host="localhost",
    password="your_password",  # Update with your MySQL password
    database="bankrecords"
)
```
### 1. User Interaction
Upon running the script, the user will be prompted with the following options:
```
1. Register: Create a new account by providing a username and password.
2. Login: Log in using an existing username and password.
3. Exit: Exit the system.
```
### 2. Once logged in, the user can perform the following actions:
```
1. Check Balance: Check the current balance of the account.
2. Deposit: Deposit a specified amount into the account.
3. Withdraw: Withdraw a specified amount from the account, if the balance is sufficient.
4. Statements: View transaction history (deposits and withdrawals).
5. Logout: Logout from the current session.
```
## Sample Output:

```
Welcome to the Banking System!
1. Register
2. Login
3. Exit
Enter your choice: 1
Enter a username: john_doe
Enter a password: password123
User registered successfully!

Welcome to the Banking System!
1. Register
2. Login
3. Exit
Enter your choice: 2
Enter your username: john_doe
Enter your password: password123
Login successful!

1. Check Balance
2. Deposit
3. Withdraw
4. Statements
5. Logout
Enter your choice: 2
Enter the amount to deposit: 500.00
Deposited $500.00 successfully!

1. Check Balance
2. Deposit
3. Withdraw
4. Statements
5. Logout
Enter your choice: 4

Transaction History:
Transaction ID      Transaction Date       Type           Amount
----------------------------------------------------------------------
1                   20-11-2024 12:00:00   deposit        $500.00
