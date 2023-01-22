import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Taylor", 27, "Saturday", 20)
        self.guest2 = Guest("Sam", 24, "Sweet Caroline", 3)
        self.room = Room(2, 5, 5)
        self.song = Song(["Saturday", "Getting Started", "Spit Of You"])
        

    def test_fav_song(self):
        actual = self.guest.check_fav_song(self.song.song_list[0])
        self.assertEqual("whooo!", actual)

    def test_pay_fee_enough_money(self):
        actual = self.guest.pay_fee(self.room.fee)
        self.assertEqual(15, actual)

    def test_pay_fee_not_enough_money(self):
        actual = self.guest2.pay_fee(self.room.fee)
        self.assertEqual("I dont have enough cash", actual)
