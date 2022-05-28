import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song({"artist": "Radiohead", "title": "My Iron Lung"})

    def test_song_has_entry(self):
        self.assertEqual({"artist": "Radiohead", "title": "My Iron Lung"}, self.song.track_info)

    # def test_song_has_title(self):
    #     self.assertEqual("My Iron Lung", self.song.title)