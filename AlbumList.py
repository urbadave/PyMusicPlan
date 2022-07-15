from ast import arg
from typing import NamedTuple
import re
import random

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

    def cloneAlbum(self, album: Album):
        return Album(album.artist, album.title, album.year, album.index)
    
    def scambleList(self, alist: list):
        #clone list
        retVal = alist.copy()
        random.seed()
        top = len(alist)-1
        #foreach item in clone
        for i in range(top):
            index = random.randint(0, top)
            save = self.cloneAlbum(retVal[i])
            retVal[i] = retVal[index]
            retVal[index] = save
        #return scrambled list
        return retVal

    def prettyAlbum(self, album: Album):
        return f'{album.artist.ljust(self.ArtistLen, " ")} {album.title.ljust(self.TitleLen, " ")} {album.year}'
    
    def prettyList(self, alist: list, addNewline: bool = False):
        prettyLines = []
        extra = ''
        if(addNewline):
            extra = '\n'
        for a in alist:
            prettyLines.append(self.prettyAlbum(a)+extra)
        return prettyLines

    def writeFile(self, alist: list, fileName: str):
        fullPath = self.createFullPath(fileName)
        linesToWrite = self.prettyList(alist, True)
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

randoList = alist.scambleList(alist.MyList)
#pretty = alist.prettyList(randoList)

pretty = alist.writeFile(randoList, "testFile.txt")

for p in pretty:
    print(p)