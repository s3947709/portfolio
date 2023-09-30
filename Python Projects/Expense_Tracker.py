def add_expense (date, category, amount):
    with open('expense.txt','a') as file:
        file.write(f"{date},{category},{amount}\n")

def view_expenses():
    with open('expense.txt','r') as file:
        expenses = file.readlines()
        if not expenses:
            print ("No expenses recorded yet.")
        else:
            print ("Date       |Category    |Amount")
            print ("-"*30)
            for expense in expenses:
                date, category, amount = expense.strip().split(',')
                print (f"{date} |   {category}  |   {amount}")

def main():
    while True:
        print ("\nExpense Tracker Menu")
        print ("1. Add Expense")
        print ("2. View Expense")
        print ("3. Quit")

        choice = input ("Enter your choice (1/2/3/): ")

        if choice == '1':
            date = input("Enter date (DD-MM-YYYY): ")
            category = input ("Enter category: ")
            amount = input ("Enter amount ($): ")
            add_expense(date,category,amount)
            print ("Expense added successfully!")

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            break

        else: 
            print ("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


 
