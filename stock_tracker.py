# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 180,
    "MSFT": 420
}

# Get stock name from user
stock_name = input(
    "Enter stock name (AAPL, TSLA, GOOGL, AMZN, MSFT): "
).upper()

# Check whether stock exists
if stock_name in stock_prices:

    # Get quantity
    quantity = int(input("Enter quantity: "))

    # Get stock price
    price = stock_prices[stock_name]

    # Calculate total investment
    total = price * quantity

    # Display result
    print("\n----- Portfolio Details -----")
    print("Stock:", stock_name)
    print("Price per share: ₹", price)
    print("Quantity:", quantity)
    print("Total Investment: ₹", total)

else:
    print("Stock not found!")