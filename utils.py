import os
from pygame import mixer
mixer.init()


def obtendo_arquivos(directory):
    directories = []
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            directories.append(root + os.sep + file)

    return directories

def play_musica(sound_path):
    mixer.music.load(sound_path)
    mixer.music.play()

def stop_musica():
    mixer.music.stop()

def pause_musica():
    mixer.music.pause()

def musica_tocando():
    if mixer.music.get_busy() == True:
        return True
    return False