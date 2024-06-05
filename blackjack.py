"""
Blackjack!

"""

from tkinter import Tk, Label, Button, Entry, Frame, PhotoImage, Canvas
from PIL import Image, ImageTk
import random, timer


#DEFINING VARIABLES
total_bet = 0
player_points = []
play=[]
dealer_points = []
new={}
playercard=[]
totals = {"player" : 0, "dealer" : 0}
deck=[]
font1=('Times',15,'bold')
font2=('Times New Roman',15,'normal') 
font3=('Times',10,'bold')

# defining our functions 
def check():
  global total_bet
  total_bet = user_bet.get()
  if total_bet.isnumeric():
	   #Switches bet to int and displays it while clearing betting input box
    total_bet = int(total_bet)
    deal_button.config(state='normal')
    label_bet2.config(text=f"Bet: ${total_bet}")
    label_bet.destroy()
    user_bet.destroy()
    next_button.destroy()


    

def deal():
  global total_bet
  #bets half of money
  total_bet /=2
  label_bet2.config(text=f"Bet: ${total_bet:.2f}")

  #enable buttons
  deal_button.config(state='disabled')
  hit_button.config(state='normal')
  stand_button.config(state='normal')

  #give dealer cards
  dealer_points.append(random.randint(1,10))
  dealer_points.append(random.randint(1,10))

  #give player cards
  playercard.append(random.randint(1,10))
  player_points.append(playercard[0])
  playercard.append(random.randint(1,10))
  player_points.append(playercard[1])
 
  label_dealer.config(text=f"Dealer's Cards: {dealer_points[0]} and hidden",font=font3)

  label_player.config(text=f"Your Cards: {player_points[0]} and {player_points[1]}\nTotal: {sum(playercard)}", font=font3)

  ###############
  if player_points[0]==10:
    player_points[0] = random.randint(10,13)
    
  if player_points[1]==10:
    player_points[1] = random.randint(10,13)
    
  #picks random card symbol
  for x in range(0,2): 
    alph = random.randint(1,4)

    if alph == 1:
      letter = 'C'
    elif alph == 2:
      letter = 'D'
    elif alph == 3:
      letter = 'S'
    elif alph == 4:
      letter = 'H'

      
    filename = "cards//%s%s.png" % (playercard[x],letter)
          
    deck.append({"filename" : filename, "value": player_points})
        
    new = deck[0]
    player_points.append(new)
    deck.pop(0)
    photo = PhotoImage(file=filename)
    new["label"] = Label(cards_frame, image=photo)        
    new["label"].photo = photo
    new["label"].grid(row=0,column=player_points.index(new))


def hit():
  
  #add a new random number to player_points
  newcard = random.randint(1,10)
  player_points.append(newcard)
  
  #######

  alph = random.randint(1,4)

  if alph == 1:
    letter = 'C'
  elif alph == 2:
    letter = 'D'
  elif alph == 3:
    letter = 'S'
  elif alph == 4:
    letter = 'H'

      
  filename = "cards//%s%s.png" % (newcard,letter)
          
  deck.append({"filename" : filename, "value": newcard})
  playercard.append(newcard)
   
  label_player.config(text="You drew: %s\nTotal: %d" % (newcard,sum(playercard)))
  
  
  new = deck[0]
  
  player_points.append(newcard)
  
  deck.pop(0)
  photo = PhotoImage(file=filename)
  new["label"] = Label(cards_frame, image=photo)        
  new["label"].photo = photo
  new["label"].grid(row=0,column=player_points.index(newcard))


  
  #    update label_win with a loss message
  if  sum(playercard) > 21:
    label_dealer.config(text="Dealer Wins!", font=font1)
    label_player.config(text="You Bust!",font=font1)
    new.clear()
    window.after(2000, reset)
    
def stand():
  

  # disable all buttons (see line 42)
  deal_button.config(state='disabled')
  hit_button.config(state='disabled')
  stand_button.config(state='disabled')
  # call the dealer_hit() function 
  dealer_hit()
  

def dealer_hit():
  global total_bet

  #update label_win with a loss message [Dealer Wins!]
  if sum(dealer_points) >= sum(playercard) and sum(dealer_points) <= 21:
    label_dealer.config(text="Dealer Wins!", font=font1)
    label_player.config(text="You Lose!",font=font1)
    window.after(2000, reset)
  
  
    
    #update label_win with a WIN message [Dealer Busts!]
  elif sum(dealer_points) > 21:
    label_dealer.config(text="Dealer Busts!",font=font1)
    label_player.config(text="You Win!",font=font1)
    window.after(2000, reset)
    total_bet += total_bet*2
    label_bet2.config(text=f"Bet: ${total_bet:.2f}")
  
 
    #add a new random number to dealer_points
  else: 
    dealer_points.append(random.randint(1,10))
    label_dealer.config(text=f"Dealer draws a {dealer_points[-1]}. Total {sum(dealer_points)}")
    window.after(2000, dealer_hit)

  

def reset():
  #disable the hit and stand buttons
  hit_button.config(state='disabled')
  stand_button.config(state='disabled')
  #enable the deal button
  deal_button.config(state='normal')
  #set player_points and dealer_points back to an empty list
  player_points.clear()
  dealer_points.clear()
  playercard.clear()
  
  #set all labels back to a default message state, either blank or "Deal to Play!"
  label_player.config(text="Blackjack!",font=font1)
  label_dealer.config(text="Press Deal to Start",font=font2) 


  global cards_frame
  # Remove the old cards_frame
  cards_frame.destroy()
  # Create a new cards_frame
  cards_frame = Frame(window)
  cards=canvas.create_window(250, 300, anchor='n', window=cards_frame)



window = Tk()

window.title("KIKI'S PLAYGROUND - BLACKJACK")  
window.geometry("600x500")
canvas = Canvas(window, width=600, height=500)
canvas.pack() 


#######BACKGROUND#######


with Image.open("Greentable.png") as img1:
    # Resize the image
  img1 = img1.resize((1400, 1500))
    # Convert the image to a PhotoImage object
  image01 = ImageTk.PhotoImage(img1)
  canvas.create_image(600, 500, image=image01)



#############################


#makes shape
canvas.create_rectangle(0, 20, 2000, 70, outline = "black", fill = "white",width = 2)

#title and total
label_player = Label(window, text="Blackjack!", font=font1)
player=canvas.create_window(500, 45, anchor='center', window=label_player)

#bet
label_bet2 = Label(window, text=f"Bet: ${total_bet}", font=font2)
bet=canvas.create_window(10, 470, anchor='w', window=label_bet2)

#subtitle and dealers total
label_dealer = Label(window, text="Press Deal to Start", font=font2)    
dealer=canvas.create_window(120, 45, anchor='center', window=label_dealer) 


cards_frame = Frame(window)
cards=canvas.create_window(250, 300, anchor='n', window=cards_frame) 

#################
#BETTING

label_bet = Label(window,text="Enter Bet", font=font1)
betting=canvas.create_window(250, 150, anchor='center', window=label_bet)

user_bet = Entry()
bet_input=canvas.create_window(250, 200, anchor='center', window=user_bet)

next_button = Button(window, text="  ENTER  ", command=check) 
next = canvas.create_window(250, 250, anchor='center', window=next_button)

###################
       #MAIN BUTTONS
deal_button = Button(window, text="  Deal ", command=deal,state='disabled')  
deal=canvas.create_window(550, 370, anchor='center', window=deal_button) 

hit_button = Button(window, text="   Hit  ", command=hit,state='disabled')
hit=canvas.create_window(550, 410, anchor='center', window=hit_button) 

stand_button = Button(window, text="Stand", command=stand,state='disabled')
stand=canvas.create_window(550, 450, anchor='center', window=stand_button) 

window.mainloop()




