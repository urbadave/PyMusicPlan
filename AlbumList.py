from typing import NamedTuple
import re

class Album(NamedTuple):
    artist: str
    title: str
    year: int
    index: int

# a1 = Album("2pac", "All Eyez On Me", 1996, 1)
# a2 = Album("Led Zeppelin", "Physical Graphiti", 1975, 136)
# a3 = Album("Led Zeppelin", "IV", 1971, 135)
class AlbumList:
    def __init__(self):
        self.MyList = []
    
    def addAlbum(self, album: Album):
        if(album not in self.MyList):
            self.MyList.append(album)
    
    def loadFromFile(self, filePath: str):
        with open(filePath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                sp = re.split("\t+", line)
                #print(sp)
                self.addAlbum(Album(sp[0], sp[1], int(sp[2]), int(sp[3])))


alist = AlbumList()
fp = r"C:\Users\urban\Documents\MusicAlbums\Music Albums - Albums.tsv"
alist.loadFromFile(fp)
print("There are", len(alist.MyList), "albums")
for a in alist.MyList:
    print(a)