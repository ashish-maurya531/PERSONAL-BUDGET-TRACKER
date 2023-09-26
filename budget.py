import os
from tabulate import tabulate

# Initialize budget and transactions
budget = 0
transactions = []

# Check if the data file exists and load previous transactions
data_file = "internship/1-coding-raja/budget_data.txt"
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            category, amount, transaction_type = line.strip().split(",")
            transactions.append({"category": category, "amount": float(amount), "type": transaction_type})
            if transaction_type == "Income":
                budget += float(amount)
            elif transaction_type == "Expense":
                budget -= float(amount)

# Function to display the current budget
def display_budget():
    global budget
    print(f"Current Budget: \u20B9 {budget:.2f}")

# Function to display all transactions in tabular form
def display_all_transactions():
    global budget
    print("All Transactions:")
    trans_table = [["Category", "Amount", "Type"]]
    total_income = 0
    total_expense = 0

    for transaction in transactions:
        trans_table.append([transaction['category'], f"\u20B9 {transaction['amount']:.2f}", transaction['type']])
        if transaction['type'] == 'Income':
            total_income += transaction['amount']
        elif transaction['type'] == 'Expense':
            total_expense += transaction['amount']

    print(tabulate(trans_table, headers="firstrow", tablefmt="grid"))
    print(f"Total Income: \u20B9 {total_income:.2f}")
    print(f"Total Expense: \u20B9 {total_expense:.2f}")

# Function to display all expenses, categorized and as a bill
def display_all_expenses():
    global budget
    expense_categories = {}
    total_expense = 0

    for transaction in transactions:
        if transaction['type'] == 'Expense':
            category = transaction['category']
            amount = transaction['amount']
            total_expense += amount

            if category in expense_categories:
                expense_categories[category] += amount
            else:
                expense_categories[category] = amount

    print("Expense Bill:")
    expense_table = [["Category", "Amount"]]
    for category, amount in expense_categories.items():
        expense_table.append([category, f"\u20B9 {amount:.2f}"])
    
    if expense_categories:
        most_expensive_category = max(expense_categories, key=expense_categories.get)
        least_expensive_category = min(expense_categories, key=expense_categories.get)
        print(f"Most Expensive Category: {most_expensive_category} (\u20B9 {expense_categories[most_expensive_category]:.2f})")
        print(f"Least Expensive Category: {least_expensive_category} (\u20B9 {expense_categories[least_expensive_category]:.2f})")

    expense_table.append(["Total Expense", f"\u20B9 {total_expense:.2f}"])
    print(tabulate(expense_table, headers="firstrow", tablefmt="grid"))

# Function to enter a new transaction
def enter_transaction():
    global budget
    transaction_type_input = input("Is this an Expense (E) or Income (I)? ").lower()
    if transaction_type_input in ["e", "expense"]:
        transaction_type = "Expense"
        category = input("Enter category (e.g., Groceries, Rent): ")
    elif transaction_type_input in ["i", "income"]:
        transaction_type = "Income"
        category = "Salary"  # Default category for income
    else:
        print("Invalid transaction type. Please choose 'Expense' or 'Income'.")
        return

    amount = float(input("Enter amount: \u20B9 "))

    if transaction_type == "Income":
        budget += amount
    elif transaction_type == "Expense":
        budget -= amount

    transactions.append({"category": category, "amount": amount, "type": transaction_type})
    with open(data_file, "a") as file:
        file.write(f"{category},{amount},{transaction_type}\n")

    print("Transaction recorded successfully.")
    display_budget()

# Main menu
while True:
    print("\nPersonal Budget Tracker")
    print("1. Display Budget")
    print("2. Display All Transactions")
    print("3. Display All Expenses")
    print("4. Enter Transaction")
    print("5. Exit")

    choice = input("Select an option (1/2/3/4/5): ")

    if choice == "1":
        display_budget()
    elif choice == "2":
        display_all_transactions()
    elif choice == "3":
        display_all_expenses()
    elif choice == "4":
        enter_transaction()
    elif choice == "5":
        print("Exiting the budget tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
