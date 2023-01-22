class Guest:
    def __init__(self, name, age, fav_song, wallet):
        self.name = name
        self.age = age
        self.fav_song = fav_song
        self.wallet = wallet

    def check_fav_song(self, song):
        if self.fav_song == song:
            return "whooo!"

    def pay_fee(self, amount):
        if self.wallet < amount:
            return "I dont have enough cash"
        self.wallet -= amount
        return self.wallet
        
