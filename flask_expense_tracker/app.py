from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)
FILENAME = 'expenses.csv'

def load_expenses():
    expenses = []
    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    date, item, amount = row
                    expenses.append((date, item, amount))
    except FileNotFoundError:
        pass
    return expenses

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        item = request.form["item"]
        amount = request.form["amount"]
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(FILENAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, item, amount])
        return redirect("/")
    
    expenses = load_expenses()
    try:
        total = sum(float(row[2]) for row in expenses if len(row) == 3)
    except ValueError:
        total = 0
    return render_template("index.html", expenses=expenses, total=total)


if __name__ == "__main__":
    app.run(debug=True)