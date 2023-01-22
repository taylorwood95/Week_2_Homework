import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest = Guest(name="Taylor", age=27, fav_song="Saturday", wallet=20)
        self.room = Room(number=2, capacity=5, fee=5)
        self.song = Song(song_list = ["Saturday", "Getting Started", "Spit Of You"])

    def test_add_guest(self):
        self.room.add_guest(self.guest.name)
        self.assertEqual(["Taylor"], self.room.guest_list)

    def test_remove_guest(self):
        self.room.remove_guest(self.guest)
        self.assertEqual([], self.room.guest_list)

    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song.song_list[0])
        self.assertEqual("Saturday", self.song.song_list[0])

    def test_check_capacity(self):
        actual = self.room.check_capacity()
        self.assertEqual("You can come in", actual)
