from ast import arg
from typing import NamedTuple
import re

class Album(NamedTuple):
    artist: str
    title: str
    year: int
    index: int

class AlbumList:
    def __init__(self, path):
        self.MyList = []
        self.ArtistLen = 0
        self.TitleLen = 0
        self.Path = path
    
    def addAlbum(self, album: Album):
        if(album not in self.MyList):
            self.MyList.append(album)

    def createFullPath(self, fileName: str):
        return self.Path+"\\"+fileName
    
    def loadFromFile(self, fileName: str):
        fullPath = self.createFullPath(fileName)
        with open(fullPath, 'r', encoding='utf-8') as f:
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
        return f'{album.artist.ljust(self.ArtistLen, " ")} {album.title.ljust(self.TitleLen, " ")} {album.year}'
    
    def prettyList(self, addNewline: bool = False):
        prettyLines = []
        extra = ''
        if(addNewline):
            extra = '\n'
        for a in self.MyList:
            prettyLines.append(self.prettyAlbum(a)+extra)
        return prettyLines

    def writeFile(self, fileName: str):
        fullPath = self.createFullPath(fileName)
        linesToWrite = self.prettyList(True)
        with open(fullPath, 'w', encoding='utf-8') as f:
            f.writelines(linesToWrite)
        return linesToWrite


p = r"C:\Users\urban\Documents\MusicAlbums"
alist = AlbumList(p)
fp = r"Music Albums - Albums.tsv"
alist.loadFromFile(fp)
print("There are", len(alist.MyList), "albums")
print("Artist length is", alist.ArtistLen)
print("TItle length is", alist.TitleLen)
#pretty = alist.prettyList()

pretty = alist.writeFile("testFile.txt")

for p in pretty:
    print(p)