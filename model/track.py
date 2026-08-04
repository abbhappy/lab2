from typing import List, Optional


class Track:
    def __init__(
        self,
        track_id: str,
        title: str,
        artist: str,
        album: Optional[str] = None,
        year: Optional[int] = None,
        composers: Optional[List[str]] = None,
        lyrics: Optional[str] = None,
        duration: Optional[int] = None,
        producers: Optional[List[str]] = None,
    ):
        self._track_id = track_id
        self._title = title
        self._artist = artist
        self._album = album
        self._year = year
        self._composers = composers or []
        self._lyrics = lyrics
        self._duration = duration
        self._producers = producers or []
        self._genres = []

    @property
    def track_id(self):
        return self._track_id

    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist

    @property
    def album(self):
        return self._album

    @property
    def year(self):
        return self._year

    @property
    def composers(self):
        return self._composers

    @property
    def lyrics(self):
        return self._lyrics

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: int):
        if value < 0:
            raise ValueError("Duration cannot be negative")
        self._duration = value

    @property
    def producers(self):
        return self._producers

    @property
    def genres(self):
        return self._genres

    def add_genre(self, genre: "Genre"):
        if genre not in self._genres:
            self._genres.append(genre)
            genre.add_track(self)

    def remove_genre(self, genre: "Genre"):
        if genre in self._genres:
            self._genres.remove(genre)
            genre.remove_track(self)

    def __str__(self):
        return f"{self._title} by {self._artist} (ID: {self._track_id})"

    def __repr__(self):
        return f"Track('{self._track_id}', '{self._title}', '{self._artist}')"

    def __eq__(self, other):
        if not isinstance(other, Track):
            return False
        return self._track_id == other._track_id

    def __hash__(self):
        return hash(self._track_id)