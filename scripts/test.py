# Copyright (C) <2013>  <Yeshiwei>
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
import mkhtml
print mkhtml.syspath2webpath('/home/psy/music/Yanni/Santorini.mp3')

s=mkhtml.song('/home/alex/Music/top.mp3')
s1=mkhtml.song('/home/alex/Music/time.mp3')
print s.jscode
print isinstance(s,mkhtml.song)

c=mkhtml.song_collection([s])
print c.getjscode()
c.addsong(s1)

print c.getjscode()

A=mkhtml.Album([s])
A.addsong(s)
print A.jscode
