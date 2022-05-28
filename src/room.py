class Room:
    def __init__(self, number, fee, capacity, till):
        self.number = number
        self.fee = fee
        self.capacity = capacity
        self.till = till
        self.playlist = []
        self.guests = []
    
    def add_song(self, song):
        self.playlist.append(song)

    def charge_entry(self, guest, fee):
        self.till += fee
        guest.pay_entry(fee)

    def add_guest(self, guest):
        self.guests.append(guest.name)

    def remove_guest(self, guest_name):
        self.guests.remove(guest_name)

    def remove_all_guests(self):
        self.guests.clear()

    def check_capacity(self, group_size):
        return group_size <= self.capacity

    def check_in(self, guest):
        self.add_guest(guest)
        self.charge_entry(guest, self.fee)

    def search_playlist(self, searched_title):
        for song in self.playlist:
            return song.track_info["title"] == searched_title

