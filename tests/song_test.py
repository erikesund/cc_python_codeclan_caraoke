import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Radiohead", "My Iron Lung")

    def test_song_has_artist(self):
        self.assertEqual("Radiohead", self.song.artist)

    def test_song_has_title(self):
        self.assertEqual("My Iron Lung", self.song.title)