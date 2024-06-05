from tkinter import Tk, Label, Button, Entry, Frame, PhotoImage, Canvas
import tkinter as tk
from PIL import Image, ImageTk
import random, timer

#Moves onto blackjack intro
def bj_intro():
  games.destroy()
  import bjintro

#displays text when hovering over game buttons
def show_description(event):
    subtitle.config(text='COMING SOON!')
def hide_description(event):
    subtitle.config(text="")
  
def show_description2(event):
    subtitle.config(text='PLAY NOW!')
def hide_description2(event):
    subtitle.config(text="")
# create the games
games = Tk()
games.title("KIKI'S PLAYGROUND")  
games.geometry("500x400")
# create a canvas
canvas = Canvas(games, width=500, height=400)
canvas.pack() 

title = Label(games, text="KIKI'S GAMES",font=("Times New Roman", 20))
player=canvas.create_window(250, 30, anchor='center', window=title)


subtitle = Label(games, text="",font=("Times New Roman", 10))
player=canvas.create_window(250, 60, anchor='center', window=subtitle)

### logo ###
imagelogo = Image.open("Kick5.gif")
imagelogo = imagelogo.resize((80,70))

logo = ImageTk.PhotoImage(imagelogo)

logo_button = Label(games,image=logo)
button_games01 = canvas.create_window(45, 30, anchor='center', window=logo_button)



### GO FISH ###
image1 = Image.open("gofish.png")
image1 = image1.resize((130,130))

gofish = ImageTk.PhotoImage(image1)

gofish_button = Button(games,image=gofish)

button_games1 = canvas.create_window(400, 200, anchor='center', window=gofish_button)

gofish_button.bind('<Enter>', show_description)
gofish_button.bind('<Leave>', hide_description)

### UNO ###
image2 = Image.open("uno.png")
image2 = image2.resize((130,130))

uno = ImageTk.PhotoImage(image2)

uno_button = Button(games,image=uno)

button_games2 = canvas.create_window(250, 200, anchor='center', window=uno_button)

uno_button.bind('<Enter>', show_description)
uno_button.bind('<Leave>', hide_description)

### BLACK JACK ###
image3 = Image.open("blackjack.png")
image3 = image3.resize((130,130))

blackjack = ImageTk.PhotoImage(image3)

blackjack_button = Button(games,image=blackjack, command=bj_intro)

button_games3 = canvas.create_window(100, 200, anchor='center', window=blackjack_button)

blackjack_button.bind('<Enter>', show_description2)
blackjack_button.bind('<Leave>', hide_description2)

######### other games ############
### GAME 1 ###
image4 = Image.open("G1.jpg")
image4 = image4.resize((65,65))

game1 = ImageTk.PhotoImage(image4)

game1_button = Button(games,image=game1)

button_othergames = canvas.create_window(65, 330, anchor='center', window=game1_button)

game1_button.bind('<Enter>', show_description)
game1_button.bind('<Leave>', hide_description)


### GAME 2 ###

image5 = Image.open("G2.jpg")
image5 = image5.resize((65,65))

game2 = ImageTk.PhotoImage(image5)

game2_button = Button(games,image=game2)

button_othergames2 = canvas.create_window(138, 330, anchor='center', window=game2_button)

game2_button.bind('<Enter>', show_description)
game2_button.bind('<Leave>', hide_description)


### GAME 3 ###


image6 = Image.open("G3.jpg")
image6 = image6.resize((65,65))

game3 = ImageTk.PhotoImage(image6)

game3_button = Button(games,image=game3)

button_othergames3 = canvas.create_window(213, 330, anchor='center', window=game3_button)

game3_button.bind('<Enter>', show_description)
game3_button.bind('<Leave>', hide_description)


### GAME 4 ###


image7 = Image.open("G4.jpg")
image7 = image7.resize((65,65))

game4 = ImageTk.PhotoImage(image7)

game4_button = Button(games,image=game4)

button_othergames4 = canvas.create_window(287, 330, anchor='center', window=game4_button)

game4_button.bind('<Enter>', show_description)
game4_button.bind('<Leave>', hide_description)




### GAME 5 ###
image8 = Image.open("G5.jpg")
image8 = image8.resize((65,65))

game5 = ImageTk.PhotoImage(image8)

game5_button = Button(games,image=game5)

button_othergames5 = canvas.create_window(362, 330, anchor='center', window=game5_button)

game5_button.bind('<Enter>', show_description)
game5_button.bind('<Leave>', hide_description)


### GAME 6 ###
image9 = Image.open("G6.jpg")
image9 = image9.resize((65,65))

game6 = ImageTk.PhotoImage(image9)

game6_button = Button(games,image=game6)

button_othergames6 = canvas.create_window(435, 330, anchor='center', window=game6_button)

game6_button.bind('<Enter>', show_description)
game6_button.bind('<Leave>', hide_description)


# start the main loop
games.mainloop()
