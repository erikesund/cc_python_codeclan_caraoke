import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar 

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room(1, 5, 3, 0)
        self.room_2 = Room(2, 5, 5, 0)

        self.guest_1 = Guest("Thom Yorke", 53, "Believe", 1000)
        self.guest_2 = Guest("Jonny Greenwood", 50, "Barbie Girl", 200)
        self.guest_3 = Guest("Ed O'Brian", 54, "Back in Black", 4)
        self.guest_4 = Guest("Phil Selway", 55, "Wind of Change", 15)
        self.guest_5 = Guest("Colin Greenwood", 52, "My Iron Lung", 16)

        self.song_1 = Song("Radiohead", "My Iron Lung")
        self.song_2 = Song("Iron Maiden", "Back in Black")
        self.song_3 = Song("Frightened Rabbit", "State Hospital")
        self.song_4 = Song("Aqua", "Barbie Girl")
        self.song_5 = Song("The B52's", "Love Shack")

        # self.room_1.playlist = [self.song_1, self.song_2]

    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.number)
        self.assertEqual(2, self.room_2.number)

    def test_room_has_entry_fee(self):
        self.assertEqual(5, self.room_1.fee)
        self.assertEqual(5, self.room_2.fee)

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room_1.capacity)
        self.assertEqual(5, self.room_2.capacity)

    def test_can_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual([self.song_1], self.room_1.playlist)

    def test_room_can_add_second_song(self):
        self.room_1.add_song(self.song_1)
        self.room_1.add_song(self.song_3)
        self.assertEqual([self.song_1, self.song_3], self.room_1.playlist)

    def test_charge_entry(self):
        self.room_1.charge_entry(self.guest_1, self.room_1.fee)
        self.assertEqual(5, self.room_1.till)

    def test_add_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual([self.guest_1.name], self.room_1.guests)

    def test_remove_guests(self):
        self.room_1.remove_all_guests()
        self.assertEqual(0, len(self.room_1.guests))

    def test_enough_capacity__returns_false(self):
        self.assertEqual(False, self.room_1.check_capacity(4))

    def test_enough_capacity__returns_true(self):
        self.assertEqual(True, self.room_2.check_capacity(4))

    def test_check_guest_in(self):
        self.room_1.check_in(self.guest_1)
        self.room_1.check_in(self.guest_2)

        self.assertEqual(10, self.room_1.till)
        self.assertEqual([self.guest_1.name, self.guest_2.name], self.room_1.guests)

    def test_remove_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_guest(self.guest_2)
        
        self.room_1.remove_guest(self.guest_1.name)

        self.assertEqual([self.guest_2.name], self.room_1.guests)

    def test_search_playlist__found_song_true(self):
        self.room_1.add_song(self.song_1)
        result_true = self.room_1.search_playlist_by_title(self.song_1.title)
        self.assertEqual(True, result_true)

    def test_search_playlist__found_song_false(self):
        self.room_1.add_song(self.song_2)
        result_false = self.room_1.search_playlist_by_title(self.song_1.title)
        self.assertEqual(False, result_false)

    def test_can_send_money_to_bar(self):
        self.room_1.till = 150
        self.bar = Bar(100)

        self.room_1.send_money_to_bar(self.room_1, self.bar)
        self.assertEqual(250, self.bar.till)
        self.assertEqual(0, self.room_1.till)


    def test_close_room(self):
        self.room_1 = Room(1, 5, 3, 100)
        self.room_1.guests = ["Ed O'Brian", "Jonny Greenwood", "Phil Selway"]
        self.room_1.till = 150
        self.bar = Bar(100)

        self.room_1.close_room(self.room_1, self.bar)

        self.assertEqual(0, len(self.room_1.guests))
        self.assertEqual(250, self.bar.till)
        self.assertEqual(0, self.room_1.till)


