from tkinter import Tk, Label, Button, Entry, Frame, PhotoImage, Canvas
import tkinter as tk
from PIL import Image, ImageTk
import random, timer

#continues
def blackjackmain():
  bj_intro.destroy()
  import blackjack

#exits program
def games():
  bj_intro.destroy()
  
  

#open black jack
# create the bj_intro
bj_intro = Tk()
bj_intro.title("KIKI'S PLAYGROUND - BLACKJACK")  
bj_intro.geometry("500x400")
# create a canvas
canvas = Canvas(bj_intro, width=500, height=400)
canvas.pack() 

with Image.open("blackjackintro.jpg") as img1:
    # Resize the image
    img1 = img1.resize((500, 400))
    # Convert the image to a PhotoImage object
    image01 = ImageTk.PhotoImage(img1)
    canvas.create_image(250, 200, image=image01)




play_button = Button(bj_intro, text="   PLAY   ",font=("Helvetica", 20), command=blackjackmain) 
play = canvas.create_window(250, 190, anchor='center', window=play_button)



exit_button = Button(bj_intro, text="    EXIT   ",font=("Helvetica", 20), command=games) 
exit = canvas.create_window(250, 250, anchor='center', window=exit_button)

bj_intro.mainloop()

