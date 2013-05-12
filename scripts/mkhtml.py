#coding=utf-8

# Copyright (C) <2013>  <Hörmetjan Yiltiz, Yeshiwei>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os, eyeD3, uuid
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

sysroots = [config.get('main', 'sysroots')]
searchpath = [config.get('main', 'searchpath')]
webroot = config.get('main', 'webroot')
default_poster= config.get('main', 'default_poster')

LICENSE_TERM = """
<cloudmusicbox>  Copyright (C) <2013>  <Hörmetjan, Yeshiwei>'
This program comes with ABSOLUTELY NO WARRANTY; for details see LICENSE'
This is free software, and you are welcome to redistribute it'
under certain conditions; see LICENSE for details.'
"""
print(LICENSE_TERM)

def mystr(s):
    if type(s)==type(u'a'):
        return s.encode('utf-8')
    else:
        return str(s)

def syspath2webpath(syspath):
    for root in sysroots:
        webpath=syspath.replace(root,webroot)
        if webpath!=syspath:
            return webpath
    return webroot+'top.mp3'

class song():
    def __init__(self):
        self.Title=None
        self.syspath=None
        self.webpath=None
        self.Album=None
        self.Artist=None
        self.jscode=None

    def __init__(self,syspath):
        tag= eyeD3.Tag()
        try:
            tag.link(syspath)
        except eyeD3.tag.TagException:
            print syspath, 'error'
            print 'please remove', syspath
        t=tag.getTitle()
        self.filename=syspath.split('/')[-1]
        if t:
            self.Title=t
        else:
            self.Title=self.filename
        self.syspath=syspath
        self.webpath=syspath2webpath(syspath)
        a=tag.getAlbum()
        if a:
            self.Album=a
        else:
            self.Album=syspath.split('/')[-2]
        ar=tag.getArtist()
        if ar:
            self.Artist=ar
        else:
            self.Artist=syspath.split('/')[-3]
        self.syslocation=syspath[:-len(self.filename)]
        self.jscode=None
        self.jscode=self.getjscode()

    def getjscode(self):
        if self.jscode:
            return self.jscode
        else:
            js='{\n'
            js+=('title:\"'+mystr(self.Title)+'\",\n')
            js+=('artist:\"'+mystr(self.Artist)+'\",\n')
            js+=('mp3:\"'+self.webpath[0:-3]+'mp3\",\n')
            #js+=('oga:\"'+self.webpath[0:-3]+'ogg\",\n')
            cover=self.syslocation+'cover.jpg';
            if os.path.exists(cover):
                js+=('poster:\"'+syspath2webpath(cover)+'\"\n')
            else:
                js+=('poster:\"'+ default_poster +'\"\n')
            js+=('}\n')
            return js


class song_collection():
    def __init__(self):
        self.songs=[]
        self.id=str(uuid.uuid1())

    def __init__(self, songs):
        if type(songs)!=list:
            raise('A song collection should be made by a list of songs!')
        for i in songs:
            if(not isinstance(i,song)):
                raise('A song collection should be made by a list of songs!')
        self.songs=songs
        self.id=str(uuid.uuid1())
        self.jscode=None
        self.jscode=self.getjscode()

    def getjscode(self):
        if self.jscode:
            return self.jscode
        else:
            return self.mkjs()

    def mkjs(self):
        js= "$(\"#playlist-setPlaylist-"+self.id+"\").click(function() {\n"
        js+="myPlaylist.setPlaylist([\n"
        for i in self.songs:
            js+=i.getjscode()[:-1]+',\n'
        js=js[:-2]+"\n]);\n});\n"
        return js

    def addsong(self,s):
        if not isinstance(s,song):
            raise('Please do\'t add non-song instance to song collection.')
        self.songs.append(s)
        self.jscode=self.mkjs()

class Album(song_collection):
    def __init__(self):
        song_collection.__init__(self)
        self.title=None
        self.Artist=None
        self.songs=[]
        self.htmlcode=self.mkhtml()

    def mkhtml(self):
        return "<a href=\"javascript:;\" id=\"playlist-setPlaylist-"+self.id+"\">["+mystr(self.Artist)+"-"+mystr(self.title)+"]</a>  "

    def __init__(self,songs):
        song_collection.__init__(self,songs)
        self.title=songs[0].Album
        self.Artist=songs[0].Artist
        for i in songs:
            if i.Album != self.title:
                raise('Songs from different album can not be putted in the same album!')
        self.htmlcode=self.mkhtml()

    def addsong(self,song):
        song_collection.addsong(self,song)
        if not self.title:
            self.title=song.Album
            self.Artist=song.Artist
        if song.Album != self.title:
            raise('wrong album')



class Playlist(song_collection):
    def __init__(self):
        song_collection.__init__(self)
        self.title=None
        self.htmlcode=mkhtml();

    def __init__(self,songs):
        song_collection.__init__(self,songs)
        self.title=songs[0].syspath.split('/')[-2]
        self.htmlcode=self.mkhtml();

    def mkhtml(self):
        return "<a href=\"javascript:;\" id=\"playlist-setPlaylist-"+self.id+"\">["+mystr(self.title)+"]</a>  "

def checkpath(path):
    global Allsongs
    if os.path.isdir(path):
        dirlist=os.listdir(path)
        for i in dirlist:
            checkpath(path+'/'+i)
    else:
        if path[-3:]=="mp3":
            s=song(path)
            if Allsongs:
                Allsongs.addsong(s)
            else:
                Allsongs=Playlist([s])
		Allsongs.title="所有歌曲"
		Allsongs.htmlcode=Allsongs.mkhtml();

	    if s.Album:
		if Albums.has_key(s.Album):
		    Albums[s.Album].addsong(s)
		else:
		    a=Album([s])
		    Albums.update({s.Album:a})

	    if Playlists.has_key(s.syslocation):
		Playlists[s.syslocation].addsong(s)
	    else:
		p=Playlist([s]);
		Playlists.update({s.syslocation:p})
def alljs():
    js=""
    for i in Albums:
	js+=Albums[i].jscode
    for i in Playlists:
	js+=Playlists[i].jscode
    js+=Allsongs.jscode
    return js

def allhtml():
    html="<code>"
    html+="所有歌曲："
    html+=Allsongs.htmlcode
    #html+="</br>专辑：</br>"
    #for i in Albums:
        #html+=Albums[i].htmlcode
        #html+='</br>'

    html+="</br>播放列表：</br>"
    for i in Playlists:
	html+=Playlists[i].htmlcode
	html+='</br>'
    html+="</code>"
    return html

if __name__=="__main__":
    Albums={}
    Playlists={}
    Allsongs=None
    for p in searchpath:
        checkpath(p)
    template=open('template.html','r')
    output=open('index.html','w')
    for l in template.readlines():
        if l == '//tag-playlists\n':
            output.write(alljs())
        elif l == '<!--html-->\n':
            output.write(allhtml())
        else:
            output.write(l)
    template.close()
    output.close()
