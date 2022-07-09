from typing import NamedTuple

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

alist = AlbumList()
alist.addAlbum(Album("I Fight Dragons", "Kaboom!", 2011, 110))
alist.addAlbum(Album("IAMDYNAMITE", "Supermegafantastic", 2012, 111))
alist.addAlbum(Album("Imagine Dragons", "Night Visions", 2012, 112))
alist.addAlbum(Album("Imagine Dragons", "Smoke + Mirrors", 2014, 113))
alist.addAlbum(Album("Indigo Girls", "Rites of Passage", 1992, 115))
alist.addAlbum(Album("Ingrid Michaelson", "Lights Out", 2014, 116))
alist.addAlbum(Album("INXS", "Kick", 1987, 117))
alist.addAlbum(Album("Iron & Wine", "Kiss Each Other Clean", 2011, 118))
alist.addAlbum(Album("Israel Kamakawiwo'ole", "Facing Future", 1993, 119))
alist.addAlbum(Album("Jet", "Get Born", 2003, 120))
alist.addAlbum(Album("Joe Jackson", "Look Sharp!", 1979, 121))
alist.addAlbum(Album("Jónsi", "Go", 2010, 122))
alist.addAlbum(Album("Journey", "Greatest Hits", 2006, 123))
alist.addAlbum(Album("Julian Casablancas", "Phrazes For The Young", 2009, 124))
alist.addAlbum(Album("Kansas", "Point Of Know Return", 1977, 125))
alist.addAlbum(Album("Kasabian", "Velociraptor!", 2011, 126))
alist.addAlbum(Album("Kasabian", "West Ryder Pauper Lunatic Asylum", 2009, 127))
alist.addAlbum(Album("Kate Bush", "Hounds of Love", 1985, 128))
alist.addAlbum(Album("KT Tunstall", "Eye To The Telescope", 2006, 129))
alist.addAlbum(Album("KT Tunstall", "Tiger Suit", 2010, 130))
print("There are", len(alist.MyList), "albums")