class Guest:
    def __init__(self, name, age, fav_song, funds):
        self.name = name
        self.age = age
        self.fav_song = fav_song
        self.funds = funds

    def pay_entry(self, fee):
        self.funds -= fee

    def search_for_fav_song(self, room, fav_song):
        room.search_playlist(fav_song)
        
    def check_for_favorite(self, playlist, fav_song):
        for song in playlist:
            if song["title"] == fav_song:
                return "Whoo!"
            else:
                return False
            