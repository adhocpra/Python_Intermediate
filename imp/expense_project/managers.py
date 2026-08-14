from collections import defaultdict
from functools import wraps
from models import Transaction

#validate using decorator
def validate(func):
    @wraps(func)
    def wrapper(self, amount,category):
        if amount == 0:
            print("invalid amount")
            return 
        return func(self,amount,category)
    return wrapper
#Main class 

class ExpenseManager:
    def __init__(self):
        self.expenses = [] #list of transaction objecst
        

    #-- ADD TRANSACTION--------------- 
    @validate
    def add_transaction(self, amount, category):
        t = Transaction(amount, category)
        self.expenses.append(t)
        print(f"Transaction added {t}")

#---- GENERATOR-------------------
    def transaction_history(self):
        for t in self.expenses:
            yield t

     #show all
    def show_all(self):
        print("All transactions : ")
        transactions = list(self.transaction_history())
        if not transactions:
            print("No transactions yet.")
            return
        for t in transactions:
            print(t)

# -- Monthly Report
    def monthly_report(self):
        total_income = sum(t.amount for t in self.expenses if t.amount > 0)
        total_expense = sum(t.amount for t in self.expenses if t.amount < 0)
        # gives expense for each category
        category_map = defaultdict(float)
        for t in self.expenses:
            category_map[t.category] += t.amount

        # income and expense
        print(f"Total income : {total_income}")
        print(f"Total expense : {total_expense}")
        print(f"Net of income: {total_income + total_expense}")

        print("\nCategory display")
        for key, value in category_map.items():
            print(f"{key} : {value}")

          #filter by category
    def filter_by_category(self, category):
        #filter(func, list)
        result = list(filter(lambda t: t.category == category, self.expenses))
        print(f"Transactions for category {category}")
        if not result:
            print("No transactions found for this category.")
            return
        for r in result:
            print(r)

 




