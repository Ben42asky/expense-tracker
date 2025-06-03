import csv
from datetime import datetime

FILENAME = 'expenses.csv'

def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

def add_expense():
    item = input("what did you buy? ")
    amount = input("How much did it cost? ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, item, amount])
    print("Expense added!")

def view_expenses():
    print("\nYour Expenses:")
    try:
        with open(FILENAME, mode="r") as file:
            render = csv.reader(file)
            for row in render:
                print(f"{row[0]} | {row[1]} | KES {row[2]}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()
    
    elif choice == "3":
        print("Goodbye!")
        break   
    else:
        print("Invalid choice. Try again.")