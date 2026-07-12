stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

total = 0

print("===== STOCK PORTFOLIO TRACKER =====")

n = int(input("How many stocks do you own? "))

for i in range(n):
    stock = input("Enter Stock Name: ").upper()

    if stock in stocks:
        quantity = int(input("Enter Quantity: "))
        investment = stocks[stock] * quantity
        total += investment
        print("Investment Value: $", investment)
    else:
        print("Stock not available.")

print("\nTotal Investment Value = $", total)

choice = input("Do you want to save the result? (yes/no): ").lower()

if choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Total Investment = $" + str(total))
    print("Result saved successfully!")