name, a str, the symbol of the stock which is being bought
shares, an int, the quantity which is being bought
price, a float, the price paid per share
and has a second method called cost which returns a float, the total cost paid for all stocks in the portfolio

Consider that to implement the cost method, you'll need to be storing the purchases made each time the buy method is called somewhere. You may do so by any means convenient to you.

Commit this file to your repository and push it to GitHub using GitHub Desktop, with a suitable commit message."

class Portfolio:
    def __init__(self):
        self.stocks = []

    def buy(name, shares, price):
        self.stocks.append([name, shares, price])

    def cost(self):
        amt = 0.0
        for name, share, price in self.stocks:
            amt += shares*price
        return amt