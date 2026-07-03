from tkinter import *
from PIL import ImageTk, Image
import time

window = Tk()

window.geometry('700x400')

window.title('MY Digital Clock')

logo = ImageTk.PhotoImage(Image.open("clock.jpg"))
window.iconphoto(True, logo)

window.config(bg="#dededc")


def mytime():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")

    day = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%Y")

    date = time.strftime("%A")
    zone = time.strftime("%Z")

    text_time = f"{hour}:{minute}:{second} {am_pm}"
    label_time.config(text=text_time)
    label_time.after(1000, mytime)

    text_date = f"{year}/{month}/{day}"
    label_date.config(text=text_date)

    text_zone = f"{date}, {zone}"
    label_zone.config(text=text_zone)


label_time = Label(window, text="", font=(
    "Brush Script MT", 60, 'bold'), bg="#dededc", bd=10,)
label_time.pack()

label_date = Label(window, text="", font=(
    "Brush Script MT", 50, 'bold'), bg="#dededc", bd=20, fg="#c20a0a")
label_date.pack()

label_zone = Label(window, text="", font=(
    "Brush Script MT", 40, 'bold'), bg="#dededc", bd=20, fg="#05a87d")
label_zone.pack()

mytime()

window.mainloop()
