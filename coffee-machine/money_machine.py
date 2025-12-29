class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def make_payment(self, cost, coins):
        total = 0
        for coin, count in coins.items():
            total += count * self.COIN_VALUES[coin]

        if total >= cost:
            change = round(total - cost, 2)
            self.profit += cost
            return True, change
        else:
            return False, total
