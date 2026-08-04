import pytest
from model.track import Track
from model.genre import Genre


def test_track_created_with_id_title_and_artist():
    """测试：创建Track对象时，ID、标题、艺术家被正确设置"""
    track = Track("T001", "Bohemian Rhapsody", "Queen")
    assert track.track_id == "T001"
    assert track.title == "Bohemian Rhapsody"
    assert track.artist == "Queen"


def test_track_has_default_empty_genres():
    """测试：新创建的Track，其流派列表默认为空"""
    track = Track("T002", "Imagine", "John Lennon")
    assert track.genres == []


def test_track_can_add_genre():
    """测试：可以向Track添加一个Genre对象"""
    track = Track("T003", "Billie Jean", "Michael Jackson")
    pop_genre = Genre("G001", "Pop")

    track.add_genre(pop_genre)

    assert pop_genre in track.genres
    assert track in pop_genre.tracks
    assert len(track.genres) == 1


def test_track_can_remove_genre():
    """测试：可以从Track移除一个Genre对象"""
    track = Track("T004", "Hello", "Adele")
    pop_genre = Genre("G002", "Pop")

    track.add_genre(pop_genre)
    track.remove_genre(pop_genre)

    assert pop_genre not in track.genres
    assert track not in pop_genre.tracks
    assert len(track.genres) == 0


def test_track_duration_cannot_be_negative():
    """测试：时长不能为负数"""
    track = Track("T005", "Shape of You", "Ed Sheeran")
    with pytest.raises(ValueError, match="Duration cannot be negative"):
        track.duration = -10