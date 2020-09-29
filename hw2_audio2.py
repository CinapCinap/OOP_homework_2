class Track:
    def __init__(self, track_name, track_duration):
        self.track_name = track_name
        self.duration = track_duration
    def __str__(self):
        return f'{self.track_name}-{self.duration}min'
    def __lt__(self, other):
        if isinstance(other, Track):
            return self.duration < other.duration
    def __eq__(self, other):
        if isinstance(other, Track):
            return self.duration == other.duration
class Album():
    def __init__(self, band, album_name):
        self.album_name = album_name
        self.band = band
        self.track_list = []
    def __str__(self):
        tracks = '\n'
        for elm in self.track_list:
            tracks += '\t' + str(elm) + '\n'
        album_info = f'Name group: {self.band}\nName album: {self.album_name}\nTracks: {tracks}'
        return album_info     
    def add_track(self, new_track, new_duration):
        tr = Track(new_track, new_duration)
        self.track_list.append(tr)        
    def get_duration(self):
        total_duration = 0
        for elm in self.track_list:
            total_duration += elm.duration
        print(f'Album {self.album_name} duration - {total_duration} min\n')
def main():
    album1 = Album('Blue Oyster Cult', 'Fire of Unknown Origin')
    album1.add_track('Fire of Unknown Origin', 4)
    album1.add_track('Burnin\' for You', 4)
    album1.add_track('Veteran of the Psychic Wars', 5)
    print(album1)
    album1.get_duration()

    album2 = Album('Imelda May', 'Love Tattoo')
    album2.add_track('Big Bad Handsome Man', 3)
    album2.add_track('Feel Me', 2)
    album2.add_track('Smockers\' Song', 2)
    print(album2)
    album2.get_duration()

    track1 = Track('Personal Jesus', 7)
    track2 = Track('Policy of Truth', 4)
    track3 = Track('John the Revelator', 7)
    print(track1 < track2)
    print(track1 > track2)
    print(track1 == track3)
main()


