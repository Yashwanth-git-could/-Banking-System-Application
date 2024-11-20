import mysql.connector
from datetime import datetime

# MySQL connection setup
mydb = mysql.connector.connect(
    user="root",
    host="localhost",
    password="Yashwanth@7",
    database="bankrecords"
)
cursor = mydb.cursor()

def register_user(username, password):
    # Insert the user into the MySQL database
    query = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    mydb.commit()
    print("User registered successfully!")

def login_user(username, password):
    query = "SELECT user_id, balance FROM users WHERE username = %s AND password_hash = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        print("Login successful!")
        return result[0], result[1]  # Return user_id and balance
    else:
        print("Invalid username or password.")
        return None

def check_balance(user_id):
    query = "SELECT balance FROM users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    balance = cursor.fetchone()[0]
    print(f"Your current balance is: ${balance:.2f}")
    return balance

def deposit_money(user_id, amount):
    query = "UPDATE users SET balance = balance + %s WHERE user_id = %s"
    cursor.execute(query, (amount, user_id))
    mydb.commit()
    
    # Log the transaction
    transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction_query = "INSERT INTO transactions (user_id, type, amount, transaction_date) VALUES (%s, 'deposit', %s, %s)"
    cursor.execute(transaction_query, (user_id, amount, transaction_date))
    mydb.commit()
    print(f"Deposited ${amount:.2f} successfully!")
def withdraw_money(user_id, amount):
    balance = check_balance(user_id)
    if balance >= amount:
        query = "UPDATE users SET balance = balance - %s WHERE user_id = %s"
        cursor.execute(query, (amount, user_id))
        mydb.commit()
        
        transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        transaction_query = "INSERT INTO transactions (user_id, type, amount, transaction_date) VALUES (%s, 'withdrawal', %s, %s)"
        cursor.execute(transaction_query, (user_id, amount, transaction_date))
        mydb.commit()
        print(f"Withdrew ${amount:.2f} successfully!")
    else:
        print("Insufficient balance.")

def statements(user_id):
    """Displays transaction history for a user."""
    statements_query = """
        SELECT transaction_id, type, amount, transaction_date
        FROM transactions
        WHERE user_id = %s
        ORDER BY transaction_date DESC
    """
    cursor.execute(statements_query, (user_id,))
    transactions = cursor.fetchall()

    if transactions:
        print("\nTransaction History:")
        print(f"{'Transaction ID':<20}{'Transaction Date':<25}{'Type':<15}{'Amount':<10}")
        print("-" * 70)
        for transaction in transactions:
            # Format the date for better readability
            transaction_date = transaction[3].strftime('%d-%m-%Y %H:%M:%S')
            print(f"{transaction[0]:<20}{transaction_date:<25}{transaction[1]:<15}${transaction[2]:.2f}")
    else:
        print("No transactions found.")

def main():
    print("Welcome to the Banking System!")
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            register_user(username, password)
        
        elif choice == 2:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = login_user(username, password)
            
            if user:
                user_id, balance = user
                while True:
                    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Statements\n5. Logout")
                    action = int(input("Enter your choice: "))
                    
                    if action == 1:
                        check_balance(user_id)
                    elif action == 2:
                        amount = float(input("Enter the amount to deposit: "))
                        deposit_money(user_id, amount)
                    elif action == 3:
                        amount = float(input("Enter the amount to withdraw: "))
                        withdraw_money(user_id, amount)
                    elif action == 4:
                        statements(user_id)
                    elif action == 5:
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid choice!")
        elif choice == 3:
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
