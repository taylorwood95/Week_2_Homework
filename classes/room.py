class Room:
    def __init__(self, number, capacity, fee):
        self.number = number
        self.capacity = capacity
        self.guest_list = []
        self.song_list = []
        self.fee = fee

    def add_guest(self, guest):
        self.guest_list.append(guest)

    def remove_guest(self, guest):
        if guest in self.guest_list:
            self.guest_list.remove(guest)

    def add_song_to_room(self, songs):
        self.song_list.append(songs)

    def check_capacity(self):
        if len(self.guest_list) >= self.capacity:
            return "No entry"
        return "You can come in"
