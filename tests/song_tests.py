import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Taylor", 27, "Saturday", 20)
        self.room = Room(2, 5, 5)
        self.song = Song(["Saturday","Getting Started","Spit Of You"])

    
