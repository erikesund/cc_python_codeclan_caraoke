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

    def remove_guests(self):
        self.guests.clear()