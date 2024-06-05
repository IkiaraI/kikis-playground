from tkinter import Tk, Label, Button, Entry, Frame, PhotoImage, Canvas
from PIL import Image, ImageTk, ImageSequence
import random, timer, time

#moves onto games window
def games():
  window.destroy()
  import game




window = Tk()
canvas = Canvas(window, bg='white', width=500, height=500)
canvas.pack() 

#############################
window.title("KIKI'S PLAYGROUND")  
window.geometry("500x500")


win_label = Label(window)
winn = canvas.create_window(250, 200, anchor='center', window=win_label)
start_button = Button(window, text = "START", fg="white", font = ("Consolas",20),bg = "#7366f9", activebackground = "#fe5bfc", command=games)
start = canvas.create_window(250, 350, anchor='center', window=start_button)


#Imports gif
img = Image.open('Kick5.gif')
for i in range(20):
  
  for image in ImageSequence.Iterator(img):
    time.sleep(0.5)
    k = ImageTk.PhotoImage(image)
    win_label.config(image = k)
    window.update()


window.mainloop()


