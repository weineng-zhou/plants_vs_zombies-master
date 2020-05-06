import pygame as pg
from source.main import main

# add BGM by weineng zhou
pg.mixer.init()
pg.mixer.music.load('resources/music/bgm.wav')
pg.mixer.music.play()

if __name__=='__main__':
    main()
    pg.quit()

    
