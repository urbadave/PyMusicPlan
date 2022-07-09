from typing import NamedTuple

class Album(NamedTuple):
    artist: str
    title: str
    year: int
    index: int

a1 = Album("2pac", "All Eyez On Me", 1996, 1)
print(a1)
print(a1.artist)
