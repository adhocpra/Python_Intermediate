from managers import ExpenseManager
from storage import Storage

def main():
    manager= ExpenseManager()
    manager.expenses= Storage.load()

    while True:
        print("\n==== Expense Tracker=====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. Monthly Report")
        print("5. Filter BY Category")
        print("6. Save and Exit")

        choice= input("Enter choice from (1-6) :")

        if choice== "1":
            amount= float(input("Income Amount: "))
            manager.add_transaction(amount, "Income")

        elif choice== "2":
            amount= float(input("Enter your expense:"))
            category= input("Category : ")
            manager.add_transaction(-amount, category)

        elif choice=="3":
            manager.show_all()

        elif choice== "4":
            manager.monthly_report()

        elif choice== "5":
            cat= input("Enter category : ")
            manager.filter_by_category(cat)

        elif choice== "6":
            Storage.save(manager.expenses)
            print("Exiting ....")
            break
        else:
            print("Invalid Input")
if __name__== "__main__":
    main()
    