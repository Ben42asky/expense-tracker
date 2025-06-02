import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILENAME = "expenses.csv"

def load_expenses():
    expenses = []
    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print("DEBUG:", row)  # Add this
                if len(row) == 3:
                    item, amount, date = row
                    expenses.append((date, item, float(amount)))
    except FileNotFoundError:
        print("No expense data found.")
    return expenses

def show_total(expenses):
    total = sum(amount for _, _, amount in expenses)
    print(f"\n💰 Total Spent: KES {total:.2f}")

def show_by_category(expenses):
    category_totals = defaultdict(float)
    for _, item, amount in expenses:
        category_totals[item] += amount

    print("\n📊 Spending by Category:")
    for category, total in category_totals.items():
        print(f"{category}: KES {total:.2f}")

    # Plot
    labels = list(category_totals.keys())
    values = list(category_totals.values())
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color="skyblue")
    plt.title("Expenses by Category")
    plt.ylabel("KES")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    expenses = load_expenses()
    if not expenses:
        return
    show_total(expenses)
    show_by_category(expenses)

if __name__ == "__main__":
    main()
