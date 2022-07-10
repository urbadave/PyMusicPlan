from ast import arg
from typing import NamedTuple
import re

class Album(NamedTuple):
    artist: str
    title: str
    year: int
    index: int

class AlbumList:
    def __init__(self):
        self.MyList = []
        self.ArtistLen = 0
        self.TitleLen = 0
    
    def addAlbum(self, album: Album):
        if(album not in self.MyList):
            self.MyList.append(album)
    
    def loadFromFile(self, filePath: str):
        with open(filePath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                sp = re.split("\t+", line)
                #print(sp)
                artist, title, year, index = sp
                if(len(artist) > self.ArtistLen):
                    self.ArtistLen = len(artist)
                if(len(title) > self.TitleLen):
                    self.TitleLen = len(title)
                self.addAlbum(Album(artist, title, int(year), int(index)))


alist = AlbumList()
fp = r"C:\Users\urban\Documents\MusicAlbums\Music Albums - Albums.tsv"
alist.loadFromFile(fp)
print("There are", len(alist.MyList), "albums")
print("Artist length is", alist.ArtistLen)
print("TItle length is", alist.TitleLen)
# for a in alist.MyList:
#     print(a)