import pygame, random
pygame.mixer.init()

def jukebox(event):
    music = ["resources/sound/Flamewall.mp3", "resources/sound/pvrnormal.mp3", "resources/sound/Aa.mp3"]
    random_music = random.choice(music)
    pygame.mixer.music.load(random_music)
    pygame.mixer.music.play()

def stop_music(event):
    pygame.mixer.music.stop()

