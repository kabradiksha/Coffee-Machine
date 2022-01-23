class MoneyMachine:
    Currency = '$'
    COIN_VALUE = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"money: {self.profit}{self.Currency}")

    def process_coins(self):
        print("please insert the coins.")
        for coins in self.COIN_VALUE:
            self.money_received += int(input(f"how many {coins}?")) * self.COIN_VALUE[coins]
        return self.money_received

    def make_payment(self, cost):
        money = self.process_coins()
        if money >= cost:
            change = round((money-cost), 2)
            print(f"here is {change}{self.Currency} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("sorry that's not enough money. money refunded.")
            self.money_received = 0
            return False
