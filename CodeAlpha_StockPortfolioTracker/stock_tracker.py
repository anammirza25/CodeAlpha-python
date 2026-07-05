stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 200,
    "AMZN": 170
}

total_portfolio = 0

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        total_value = stock_prices[stock_name] * quantity

        print("Stock Price:", stock_prices[stock_name])
        print("Total Value:", total_value)

        total_portfolio += total_value

        choice = input("Do you want to add another stock? (yes/no): ").lower()

        if choice == "no":
            print("Total Portfolio Value:", total_portfolio)
            break

    else:
        print("Stock not found!")