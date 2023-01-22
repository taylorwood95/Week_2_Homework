class Bar:
    def __init__(self, drinks_list):
        self.drinks_list = drinks_list
        self.till = 0

    def buy_drink(self, guest, drink_name):
        drink_cost = self.drinks_list[drink_name]
        if guest.wallet >= drink_cost:
            guest.wallet -= drink_cost
            self.till += drink_cost

            return "Enjoy!"
        return "Not enough money"
