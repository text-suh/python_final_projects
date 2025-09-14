# Simple Expense Tracker (Console App)

expenses = []

def add_expense(amount, category, note):
    expenses.append({"amount": amount, "category": category, "note": note})

def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet!\n")
    else:
        print("\n--- Expense List ---")
        for i, exp in enumerate(expenses, 1):
            print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']}")
        print("-------------------\n")

def total_expenses():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Expenses: ₹{total}\n")

while True:
    print("📌 Expense Tracker Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter amount (₹): "))
            category = input("Enter category (Food/Travel/Other): ")
            note = input("Enter note: ")
            add_expense(amount, category, note)
            print("✅ Expense added!\n")
        except ValueError:
            print("❌ Please enter a valid number for amount!\n")
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("👋 Exiting... Bye!")
        break
    else:
        print("❌ Invalid choice, try again.\n")