class Guest:
    def __init__(self, name, age, fav_song, funds):
        self.name = name
        self.age = age
        self.fav_song = fav_song
        self.funds = funds

    def pay_entry(self, fee):
        self.funds -= fee