import winsound

def creat_music():
    frequency = 300
    duration = 3000
    while frequency < 700:
        winsound.Beep(frequency, duration)
        frequency += 100
        duration -= 200
    winsound.Beep(500, 3000)
    winsound.Beep(400, 3000)


creat_music()
