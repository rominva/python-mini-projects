import winsound
import random


def creat_music():
    count = 5
    while count > 0:
        winsound.Beep(random.randint(50, 2000), random.randint(200, 1000))
        count -= 1


creat_music()
