class Song:

    count = 0
    artists = set()
    genres = set()
    genre_count = dict()
    artist_count = dict()

    def __init__(self,name,artist,genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        Song.count +=1

    @classmethod
    def add_to_genres(cls,genre):
        Song.genres.add(genre)

    @classmethod
    def add_to_artists(cls,artist):
        Song.artists.add(artist)

    @classmethod
    def add_to_genre_count(cls,genre):
        if genre in Song.genre_count.keys():
            Song.genre_count[genre] = Song.genre_count[genre] +1
        else:
            Song.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls,artist):
        if artist in Song.artist_count.keys():
            Song.artist_count[artist] = Song.artist_count[artist] +1
        else:
            Song.artist_count[artist] = 1
        

