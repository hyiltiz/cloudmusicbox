A easy and straightforward self-hosting music-box service 

--------------------
Setup instructions:

 1. make a git clone in your future music box with `git clone git://github.com/hyiltiz/cloudmusicbox.git`
 1. Create a folder named `media` in the cloned directory with `mkdir -p
    cloudmusicbox/media` and put all your musics in it. (They could be a
    directory tree whose deepest folders should contain only mp3/ogg files,
    which will be automatically transformed as a play-list.
 1. configure the path settings via `config.ini`
 1. Write up your own home page using `markdown` in `README.md`
 1. run `make` in `cloudmusicbox`
 1. Voilà! Go to the directory with your favourite browser and enjoy. You  
    can serve the web with any engine you prefer.
