import pandas as pd

# Create a list that stores the expenses of a user

expenses=[]

# Create a global variable that stores the expenses throughout the month

budget=None

# Get user input for expense
# 1.ADD EXPENSE

def input_expense():
    name=input("Enter Expense name : ")
    date=input("Enter date (YYYY-MM-DD) : ")
    category=input("Category of input : ")
    description=input("Provide description of expense : ")
    
    # if amount is not a float value then show error

    while True:
        try:
            amount=float(input("Enter amount spent : "))
            break
        except ValueError:
            print("Invalid input ! ")

    # Store the expense of a user in a dictionary

    exp={'Name':name,'Date':date, 'Category':category, 'Amount Spent':amount, 'Description':description}

    # Add the expense 'exp' of the user to the list of expenses 'expenses[]'

    expenses.append(exp)
    print("Expense added successfully")

# 2.VIEW EXPENSE

def view_expenses():

    # Create a list of required fields that must be filled. if any of them is missing an error is generated

    required_fields=['Name','Date','Category','Amount Spent', 'Description']

    # if there is no expense recorded yet
    if not expenses:
        print("No expenses recorde yet.")
    # if there are expenses recorder
    else:
        print("\nList of Expenses:")
        # for loop to display the expenses providing indexing using the enumerate() function
        for i ,expense in enumerate(expenses,1):
            req=True
            # for loop to check if expense contains all the required fields
            for fields in required_fields:
                if not expense.get(fields):
                    req=False
                    break

            if req:
                print(f"\nExpense {i}:{expense}")
            else:
                print("Requirements not filled correctly ! ")

# Setting the budget for a month and tracking throughout the expenses are made.

def set_monthly_budget():
    global budget
    while True:
        try:
            budget=float(input("Enter the budget fo this month : "))
            print(f"Monthly budget set successfully ! ")
            break
        except ValueError:
            print("Invalid Input ! ")

# Track the budget througout the month

def track_budget():
    total_expense=0
    if budget is None:
        print("Please enter the monthly budget first.")
    else:
        for i in expenses:
            total_expense+=float(i['Amount Spent'])

        track=budget-total_expense
        if(track>0):
            print(f"You spent rupees {total_expense} and have ruppes {track} left")
        else:
            print(f"You have exceeded your budget by {abs(track)}")

# After expense is successfully recoded it must be stored.

# 3. SAVE AND LOAD EXPENSES

def save_expenses():
    # create a dataframe out of the expense 
    df=pd.DataFrame(expenses)

    # save that dataframe in a csv file
    csv_file_name="expenses.csv"
    df.to_csv(csv_file_name, index=False)
    print("Expense saved successfully ! ")

def load_expenses():
    csv_file_name="expenses.csv"
    try:
        df=pd.read_csv(csv_file_name)
        # store the dataframes back to dictionary
        expenses=df.to_dict('records')
        print("Expenses loaded successfully ! ")
        return expenses
    except FileNotFoundError:
        print("No expenses found.")
        return []




