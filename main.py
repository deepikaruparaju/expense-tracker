from tracker import add_expense, view_expenses, total_by_month, delete_expense, authenticate

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total by Month")
        print("4. Delete an Expense")  
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            amount = float(input("Amount (₹): "))
            category = input("Category (e.g., Food, Travel): ")
            note = input("Note: ")
            add_expense(amount, category, note)

        elif choice == '2':
            if authenticate():
                print("🔑 Authentication successful!")
                view_expenses()

        elif choice == '3':
            if authenticate():
                print("🔑 Authentication successful!")
                month = input("Enter month (YYYY-MM): ")
                total_by_month(month)

        elif choice == '4':
            if authenticate():
                print("🔑 Authentication successful!")
                delete_expense()

        elif choice == '5':
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
