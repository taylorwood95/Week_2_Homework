import unittest

from classes.bar import Bar
from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestBar(unittest.TestCase):
    def setUp(self):
        drinks_list = {"Tennents": 3, "San Miguel": 4, "Peroni": 5}
        self.bar = Bar(drinks_list=drinks_list)
        self.guest = Guest(name="Taylor", age=27, fav_song="Saturday", wallet=20)
        self.room = Room(number=2, capacity=5, fee=5)
        self.song = Song(song_list=["Saturday", "Getting Started", "Spit Of You"])

    def test_buy_drink_enough_money(self):
        actual = self.bar.buy_drink(guest=self.guest, drink_name="Tennents")
        self.assertEqual("Enjoy!", actual)
        self.assertEqual(3, self.bar.till)
        self.assertEqual(17, self.guest.wallet)
