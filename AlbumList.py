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

    def prettyAlbum(self, album: Album):
        return f'{str.ljust(album.artist, self.ArtistLen)} {str.ljust(album.title, self.TitleLen)} {album.year}'
    
    def prettyList(self):
        prettyLines = []
        for a in self.MyList:
            prettyLines.append(self.prettyAlbum(a))
        return prettyLines


alist = AlbumList()
fp = r"C:\Users\urban\Documents\MusicAlbums\Music Albums - Albums.tsv"
alist.loadFromFile(fp)
print("There are", len(alist.MyList), "albums")
print("Artist length is", alist.ArtistLen)
print("TItle length is", alist.TitleLen)
pretty = alist.prettyList()

for p in pretty:
    print(p)