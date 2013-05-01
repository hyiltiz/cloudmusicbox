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
