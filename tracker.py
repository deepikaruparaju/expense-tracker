import json
from datetime import datetime

DATA_FILE = 'data/expenses.json'
def authenticate():
    PASSWORD = "deepu123"  # 🔐 You can change this
    attempt = input("🔒 Enter password to continue: ")
    if attempt == PASSWORD:
        return True
    else:
        print("❌ Incorrect password. Access denied.")
        return False


def load_expenses():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

def add_expense(amount, category, note, date=None):
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    }
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    for exp in expenses:
        print(f"{exp['date']} | ₹{exp['amount']} | {exp['category']} - {exp['note']}")

def total_by_month(month):
    expenses = load_expenses()
    total = sum(exp['amount'] for exp in expenses if exp['date'].startswith(month))
    print(f"💰 Total for {month}: ₹{total}")
def delete_expense():
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses to delete.")
        return

    print("\n📋 Expenses:")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. {exp['date']} | ₹{exp['amount']} | {exp['category']} - {exp['note']}")

    try:
        index = int(input("\nEnter the number of the expense to delete: "))
        if 1 <= index <= len(expenses):
            removed = expenses.pop(index - 1)
            save_expenses(expenses)
            print(f"✅ Deleted: ₹{removed['amount']} | {removed['category']} - {removed['note']}")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")
