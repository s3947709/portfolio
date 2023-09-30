def add_purchase (category, amount):
    with open('profittracker.txt') as file:
        file.write(f"{category},{amount}\n")

def add_resale (category, amount):
    with open('profittracker.txt') as file:
        file.write (f"{category},{amount}")

def profit_margin (category, amount):
    with open('profittracker.txt') as file:
        file.write (f"{category},{amount}")

def main():
    while True:
        print ("\nProfit Tracker")
        print ("1. Add Purchase ")
        print ("2. Add Sell ")
        print ("3. View Profits ")
        print ("4. Exit ")

        choice = input ("Enter your choice (1/2/3/4)")

        if choice == 1:
            category = input ("What was the item: ")
            amount = input ("How much was the item: ")
            add_purchase (category,amount)


        elif choice == 2:
            category = input ("What was the item: ")
            amount = input ("How much did you sell it for: ")
            add_resale (category,amount)

        elif choice == 3:
            add_resale - add_purchase