from typing import List


class Genre:
    def __init__(self, genre_id: str, name: str):
        self._genre_id = genre_id
        self._name = name
        self._tracks = []

    @property
    def genre_id(self):
        return self._genre_id

    @property
    def name(self):
        return self._name

    @property
    def tracks(self):
        return self._tracks

    def add_track(self, track: "Track"):
        if track not in self._tracks:
            self._tracks.append(track)

    def remove_track(self, track: "Track"):
        if track in self._tracks:
            self._tracks.remove(track)

    def track_count(self):
        return len(self._tracks)

    def __str__(self):
        return f"{self._name} ({self.track_count()} track(s))"

    def __repr__(self):
        return f"Genre('{self._genre_id}', '{self._name}')"

    def __eq__(self, other):
        if not isinstance(other, Genre):
            return False
        return self._genre_id == other._genre_id

    def __hash__(self):
        return hash(self._genre_id)