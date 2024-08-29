"""A class to instantiate a song."""

class Song:
    """Building song metadata."""

    def __init__(self, title, artist, album, year):
        """Initialize title, artist, album, and year attributes."""
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
    
    def display_song(self):
        """Display values for song object."""
        song = {
            'Title': f'{self.title}',
            'Artist': f'{self.artist}',
            'Album': f'{self.album}',
            'Year': f'{self.year}'
        }
        for key, value in song.items():
            print(f"{key}: {value}")
        return song