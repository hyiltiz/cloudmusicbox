#! /usr/bin/python2

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
import os


def checkpath(path):
    global Allsongs
    if os.path.isdir(path):
        os.chdir(path)
        dirlist = os.listdir(path)
        for i in dirlist:
            checkpath(path+'/'+i)

    else:
        if path[-4:] == ".mp3" and not os.path.exists(path[:-4]+'.ogg'):
            os.system('mp32ogg '+path)


checkpath('/home/psy/music/media/Music/Yanni-Selections')
