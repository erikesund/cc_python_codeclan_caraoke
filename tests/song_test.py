import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song({"Artist": "Radiohead", "Title": "My Iron Lung"})

    def test_song_has_entry(self):
        self.assertEqual({"Artist": "Radiohead", "Title": "My Iron Lung"}, self.song.track_info)

    # def test_song_has_title(self):
    #     self.assertEqual("My Iron Lung", self.song.title)