import os
import time

from pygame import mixer

switch = 0

up = open("hele_up", "r",encoding="utf-8").read()
down = open("hele_down", "r",encoding="utf-8").read()

mixer.init()
mixer.music.load('audio.mp3')
mixer.music.play(-1)

while True:
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print(up) if switch == 0 else print(down)

    switch = 1 if switch == 0 else 0

    time.sleep(0.1)
