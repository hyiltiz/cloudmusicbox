#! /usr/bin/python2
import os


def checkpath(path):
    global Allsongs
    if os.path.isdir(path):
        os.chdir(path)
        dirlist=os.listdir(path)
        for i in dirlist:
            checkpath(path+'/'+i)

    else:
        if path[-4:]==".mp3" and not os.path.exists(path[:-4]+'.ogg'):
            os.system('mp32ogg '+path)


checkpath('/home/psy/music/media/Music/Yanni-Selections')
