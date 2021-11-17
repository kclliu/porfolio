class Portfolio:
    def __init__(self):
        self.stocks = []

    def buy(name, shares, price):
        self.stocks.append([name, shares, price])

    def cost(self):
        amt = 0.0
        for name, shares, price in self.stocks:
            amt += shares * price
        return amt