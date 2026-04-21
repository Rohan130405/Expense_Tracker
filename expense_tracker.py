import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "amount", "description"])
    except FileExistsError:
        pass


def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter category (Food/Travel/Bills): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found")


def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                date = row[0]
                amount = float(row[2])

                if date.startswith(month):
                    total += amount

        print("Total expense for", month, "is", total)

    except FileNotFoundError:
        print("No expenses found")


def category_summary():
    category_totals = {}

    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                category = row[1]
                amount = float(row[2])

                category_totals[category] = category_totals.get(category, 0) + amount

        print("\nCategory-wise Summary:")
        for category in category_totals:
            print(category, ":", category_totals[category])

    except FileNotFoundError:
        print("No expenses found")


def highest_spending_category():
    category_totals = {}

    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                category = row[1]
                amount = float(row[2])

                category_totals[category] = category_totals.get(category, 0) + amount

        if len(category_totals) == 0:
            print("No expenses found")
            return

        highest_category = max(category_totals, key=category_totals.get)
        print("Highest spending category is", highest_category, "with", category_totals[highest_category])

    except FileNotFoundError:
        print("No expenses found")


def main():
    initialize_file()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category-wise Summary")
        print("5. Highest Spending Category")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            monthly_summary()

        elif choice == 4:
            category_summary()

        elif choice == 5:
            highest_spending_category()

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice")


main()