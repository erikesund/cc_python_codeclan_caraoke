import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Thom Yorke", 53, "Believe", 1000)
        self.guest_2 = Guest("Jonny Greenwood", 50, "Barbie Girl", 200)
        self.guest_3 = Guest("Ed O'Brian", 54, "Back in Black", 4)
        self.guest_4 = Guest("Phil Selway", 55, "Wind of Change", 15)
        self.guest_5 = Guest("Colin Greenwood", 52, "My Iron Lung", 16)
        self.room_1 = Room(1, 5, 3, 0)
        self.room_2 = Room(1, 5, 5, 0)
        self.song_1 = Song("Radiohead", "My Iron Lung")
        self.song_2 = Song("Iron Maiden", "Back in Black")
        self.song_3 = Song("Radiohead", "Creep")
        self.room_1.playlist = [self.song_1, self.song_2]
        

    def test_check_guest_has_name(self):
        self.assertEqual("Thom Yorke", self.guest_1.name)
        self.assertEqual("Phil Selway", self.guest_4.name)
    
    def test_check_guest_has_age(self):
        self.assertEqual(53, self.guest_1.age)
        self.assertEqual(55, self.guest_4.age)

    def test_check_guest_has_fav_song(self):
        self.assertEqual("Believe", self.guest_1.fav_song)
        self.assertEqual("Wind of Change", self.guest_4.fav_song)

    def test_check_guest_has_funds(self):
        self.assertEqual(1000, self.guest_1.funds)
        self.assertEqual(15, self.guest_4.funds)

    def test_pay_entry(self):
        self.guest_1.pay_entry(self.room_1.fee)
        self.guest_2.pay_entry(self.room_2.fee)
        self.assertEqual(995, self.guest_1.funds)
        self.assertEqual(195, self.guest_2.funds)

    def test_check_for__favorite_is_true(self):
        result_true = self.guest_5.check_for_favorite(self.room_1, self.guest_5.fav_song)
        self.assertEqual("Whoo!", result_true)

    def test_check_for__favorite_is_false(self):
        result_false = self.guest_1.check_for_favorite(self.room_1, self.guest_1.fav_song)
        self.assertEqual(False, result_false)
    

    # def test_search_for_songs_by_artist(self):



