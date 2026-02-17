expenses = []


def add_expense(description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description} - ${amount}")


def show_expenses():
    if not expenses:
        print("No expenses yet")
        return
    print("\nExpense List:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['description']} - ${expense['amount']}")


def total():
    print(f"\nTotal: ${sum(e['amount'] for e in expenses)}")


def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Description: ")
            amount = float(input("Amount: "))
            add_expense(desc, amount)
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


main()