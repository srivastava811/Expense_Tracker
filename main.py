from expense import input_expense, view_expenses, set_monthly_budget, track_budget, save_expenses, load_expenses
def main():
    
    load_expenses()
    budget=set_monthly_budget()
    print("***EXPENSE TRACKER***")
    while True:
        n=int(input("\n 1. Add expense\n 2. View Expense\n 3. Track Budget\n 4. Save expenses\n 5. Exit\n User choice : "))
        if n==1:
            input_expense()
        elif n==2:
            view_expenses()
        elif n==3:
            track_budget()
        elif n==4:
            save_expenses()
        elif n==5:
            print("EXIT !")
            break



main()