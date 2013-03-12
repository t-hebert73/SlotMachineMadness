#Filename: slotmachine.py
#Author: Trevor Hebert
#Last Modified by: Trevor Hebert
#Date Last Modified: June 08, 2012
#Program Description: This is a slot machine game.
#Revision Version: 1.0.0
#   Revision Notes: 
# -Buttons are enabled/disabled at correct times
# -Sound added
# -Jackpot corrected and functional
# -Power button added
# -Reset button added
# 
#Revision History: 0.0.1
#                  1.0.0 - current version
#


import random
#import the Tkinter library so that it is available for use
from tkinter import *
from pygame import mixer
from tkinter import messagebox
import sys



class SlotMachine():
    

    #define the attributes of the class
    def __init__(self, myParent):
        #creates a frame whose parent is root
        self.myContainer = Frame(myParent)
        #pack the frame - show it on the screen
        self.myContainer.pack()
        
        #set the variables
        self.jackpot = 50000
        self.totalCredits = 1500
        self.bet = 0
        self.winnerpaid = 0
        
        
        def spinButtonClicked(event):
            #spin the reels if there is a bet
            if self.bet > 0 and self.totalCredits >0:
                playInfo = pullthehandle(self.bet, self.totalCredits, self.jackpot)
                Fruit_reel = playInfo[3]
                self.winnerpaid = playInfo[2]
                firstReel = Fruit_reel[0]
                secondReel = Fruit_reel[1]
                thirdReel = Fruit_reel[2]
                self.bet = playInfo[4]
                self.totalCredits = int(playInfo[0])
                
            
                #change first reel image 
                if firstReel == "Blank":
                    self.firstReelImage.configure(image=self.blankImage)
                elif firstReel == "Grapes":
                    self.firstReelImage.configure(image=self.grapeImage)
                elif firstReel == "Banana":
                    self.firstReelImage.configure(image=self.bananaImage)
                elif firstReel == "Orange":
                    self.firstReelImage.configure(image=self.orangeImage)
                elif firstReel == "Cherry":
                    self.firstReelImage.configure(image=self.cherryImage)
                elif firstReel == "Bar":
                    self.firstReelImage.configure(image=self.barImage)
                elif firstReel == "Bell":
                    self.firstReelImage.configure(image=self.bellImage)
                elif firstReel == "Seven":
                    self.firstReelImage.configure(image=self.sevenImage)
            
                #change second reel image
                if secondReel == "Blank":
                    self.secondReelImage.configure(image=self.blankImage)
                elif secondReel == "Grapes":
                    self.secondReelImage.configure(image=self.grapeImage)
                elif secondReel == "Banana":
                    self.secondReelImage.configure(image=self.bananaImage)
                elif secondReel == "Orange":
                    self.secondReelImage.configure(image=self.orangeImage)
                elif secondReel == "Cherry":
                    self.secondReelImage.configure(image=self.cherryImage)
                elif secondReel == "Bar":
                    self.secondReelImage.configure(image=self.barImage)
                elif secondReel == "Bell":
                    self.secondReelImage.configure(image=self.bellImage)
                elif secondReel == "Seven":
                    self.secondReelImage.configure(image=self.sevenImage)
                
                #change third reel image
                if thirdReel == "Blank":
                    self.thirdReelImage.configure(image=self.blankImage)
                elif thirdReel == "Grapes":
                    self.thirdReelImage.configure(image=self.grapeImage)
                elif thirdReel == "Banana":
                    self.thirdReelImage.configure(image=self.bananaImage)
                elif thirdReel == "Orange":
                    self.thirdReelImage.configure(image=self.orangeImage)
                elif thirdReel == "Cherry":
                    self.thirdReelImage.configure(image=self.cherryImage)
                elif thirdReel == "Bar":
                    self.thirdReelImage.configure(image=self.barImage)
                elif thirdReel == "Bell":
                    self.thirdReelImage.configure(image=self.bellImage)
                elif thirdReel == "Seven":
                    self.thirdReelImage.configure(image=self.sevenImage)    
            
                #update the winning, bet, credits and disable spin button
                self.winningsLabel.configure(text=self.winnerpaid)
                self.bet = 0
                self.betLabel.configure(text=self.bet)
                self.creditLabel.configure(text=self.totalCredits)
                self.spinButton.configure(state=DISABLED)
                
                #jackpot variables
                self.jackPot_flag = playInfo[5]
                self.jackpot = int(playInfo[1])
               
                #if jackpot is won update total credits
                if self.jackPot_flag == True:
                    self.totalCredits += self.jackpot
                    self.creditLabel.configure(text=self.totalCredits)
                    self.winningsLabel.configure(text=self.jackpot)
                    
                #if user runs out of credits disable buttons and notify
                if self.totalCredits <= 0:
                    self.bet10Button.configure(state=DISABLED)
                    self.bet100Button.configure(state=DISABLED)
                    self.betMaxButton.configure(state=DISABLED)
                    messagebox.showinfo("Out of Credits", "You are out of credits, press Reset to play again.")
                    
           
                
                
        def bet10ButtonClicked(event):
            if self.totalCredits >= 10:
                self.bet = 10
                self.betLabel.configure(text=self.bet)
                self.spinButton.configure(state=NORMAL)
            
        def bet100ButtonClicked(event):
            if self.totalCredits >= 100:
                self.bet = 100
                self.betLabel.configure(text=self.bet)
                self.spinButton.configure(state=NORMAL)
            
        def betMaxButtonClicked(event):
            if self.totalCredits >= 500:
                self.bet = 500
                self.betLabel.configure(text=self.bet)
                self.spinButton.configure(state=NORMAL) 
            
        def resetButtonClicked(event):
            self.totalCredits = 1500
            self.creditLabel.configure(text="1500")
            self.betMaxButton.configure(state=NORMAL)
            self.bet100Button.configure(state=NORMAL)
            self.bet10Button.configure(state=NORMAL)
            
        def powerButtonClicked(event):
            sys.exit()
            
        mixer.init(44100)    
        sound = mixer.Sound("Sounds/casino.wav")   
        sound.play(loops=-1)
        #create the canvas
        self.bg_panel = Canvas(self.myContainer, width=406, height=407, bg="blue")

        self.bg_panel.pack(expand=YES,fill=BOTH)       

        #load in images
        self.bg_img = PhotoImage(file="Images/slotmachine.gif")
        self.blankImage = PhotoImage(file="Images/blank.gif")
        self.grapeImage = PhotoImage(file="Images/grapes.gif")
        self.bananaImage = PhotoImage(file="Images/banana.gif")
        self.orangeImage = PhotoImage(file="Images/orange.gif")
        self.cherryImage = PhotoImage(file="Images/cherry.gif")
        self.barImage = PhotoImage(file="Images/bar.gif")
        self.bellImage = PhotoImage(file="Images/bell.gif")
        self.sevenImage = PhotoImage(file="Images/seven.gif")
        self.betLineImage = PhotoImage(file="Images/betline.gif")
        #create the background image
        self.bg_panel.create_image(0, 0, image = self.bg_img, anchor=NW)
        
        #create first reel label and set the image to blank
        self.firstReelImage = Label(self.myContainer, width="90",height="110")
        self.firstReelImage.configure(image=self.blankImage)
        self.firstReelImage.pack()
        self.firstReelImage.place(x=52, y=128)
        
        #create second reel label and set the image to blank
        self.secondReelImage = Label(self.myContainer, width="90",height="110")
        self.secondReelImage.configure(image=self.blankImage)
        self.secondReelImage.pack()
        self.secondReelImage.place(x=157, y=128)
        
        #create third reel label and set the image to blank
        self.thirdReelImage = Label(self.myContainer, width="90",height="110")
        self.thirdReelImage.configure(image=self.blankImage)
        self.thirdReelImage.pack()
        self.thirdReelImage.place(x=262, y=128)
                
        #Create the bet 10 button
        self.bet10Button = Button(self.myContainer)
        self.bet10Button["text"]= "Bet 10"
        self.bet10Button["background"] = "green"
        self.bet10Button.pack()
        self.bet10Button.place(x=95, y=345, height=45, width=46)
        #bind the button to a click event
        self.bet10Button.bind("<Button-1>", bet10ButtonClicked)
        
        #Create the bet 100 button
        self.bet100Button = Button(self.myContainer)
        self.bet100Button["text"]= "Bet 100"
        self.bet100Button["background"] = "green"
        self.bet100Button.pack()
        self.bet100Button.place(x=153, y=345, height=45, width=46)
        #bind the button to a click event
        self.bet100Button.bind("<Button-1>", bet100ButtonClicked)
        
        #Create the bet max button
        self.betMaxButton = Button(self.myContainer)
        self.betMaxButton["text"]= "Bet Max"
        self.betMaxButton["background"] = "green"
        self.betMaxButton.pack()
        self.betMaxButton.place(x=210, y=345, height=45, width=48)
        #bind the button to a click event
        self.betMaxButton.bind("<Button-1>", betMaxButtonClicked)
        
        #create the winning label
        self.winningsLabel = Label(self.myContainer)
        self.winningsLabel.pack()
        self.winningsLabel.configure(text=self.winnerpaid)
        self.winningsLabel.place(x=235, y=260, width=70)
        
        #create the bet label
        self.betLabel = Label(self.myContainer)
        self.betLabel.pack()
        self.betLabel.configure(text=self.bet)        
        self.betLabel.place(x=186, y=260, width=30)

        #create the credit label
        self.creditLabel = Label(self.myContainer)
        self.creditLabel.pack()
        self.creditLabel.configure(text=self.totalCredits)
        self.creditLabel.place(x=90, y=260)
        
        #create the spin button
        self.spinButton = Button(self.myContainer)
        self.spinButton["text"]= "Spin"
        self.spinButton["background"] = "blue"
        self.spinButton["fg"] = "white"
        self.spinButton.pack()
        self.spinButton.place(x=323, y=344, height=46, width=47)
        #bind the spin button to a click and enter event
        self.spinButton.bind("<Button-1>", spinButtonClicked)
        #disable spin button
        self.spinButton.configure(state=DISABLED)
        
        #create the reset button
        self.resetButton = Button(self.myContainer)
        self.resetButton["text"]= "Reset"
        self.resetButton["fg"] = "white"
        self.resetButton["background"] = "black"
        self.resetButton.pack()
        self.resetButton.place(x=36, y=345, height=46, width=47)
        self.resetButton.bind("<Button-1>", resetButtonClicked)
        
        #create the power button
        self.powerButton = Button(self.myContainer)
        self.powerButton["text"]= "Power"
        self.powerButton["fg"] = "white"
        self.powerButton["background"] = "red"
        self.powerButton.pack()
        self.powerButton.place(x=317, y=248, height=56, width=47)
        self.powerButton.bind("<Button-1>", powerButtonClicked)
        self.powerButton["relief"] = "ridge"
        
        #create the bet line
        self.betLineLabel = Label()
        self.betLineLabel.pack()
        self.betLineLabel.configure(image=self.betLineImage, width=300, height=1, background="black")
        self.betLineLabel.place(x=52, y=185)
        
def Reels():
    """ When this function is called it determines the Bet_Line results.
        e.g. Bar - Orange - Banana """
        
    # [0]Fruit, [1]Fruit, [2]Fruit
    Bet_Line = [" "," "," "]
    Outcome = [0,0,0]
    
    # Spin those reels
    for spin in range(3):
        Outcome[spin] = random.randrange(1,65,1)
        # Spin those Reels!
        if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
            Bet_Line[spin] = "Blank"
        if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
            Bet_Line[spin] = "Grapes"
        if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
            Bet_Line[spin] = "Banana"
        if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
            Bet_Line[spin] = "Orange"
        if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
            Bet_Line[spin] = "Cherry"
        if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
            Bet_Line[spin] = "Bar"
        if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
            Bet_Line[spin] = "Bell"  
        if Outcome[spin] == 64:                         # 1.56%  Chance
            Bet_Line[spin] = "Seven"    

    
    return Bet_Line

def is_number(Bet):
    """ This function Checks if the Bet entered by the user is a valid number """
    try:
        int(Bet)
        return True
    except ValueError:
        print("Please enter a valid number or Q to quit")
        return False

def pullthehandle(Bet, Player_Money, Jack_Pot):
    """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random Bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
    Player_Money -= Bet
    
    Jack_Pot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
    win = False
    JackPot_Flag = False
    Fruit_Reel = Reels()
    Fruits = Fruit_Reel[0] + " - " + Fruit_Reel[1] + " - " + Fruit_Reel[2]
    winnings = 0
    # Match 3
    if Fruit_Reel.count("Grapes") == 3:
        winnings,win = Bet*20,True
    elif Fruit_Reel.count("Banana") == 3:
        winnings,win = Bet*30,True
    elif Fruit_Reel.count("Orange") == 3:
        winnings,win = Bet*40,True
    elif Fruit_Reel.count("Cherry") == 3:
        winnings,win = Bet*100,True
    elif Fruit_Reel.count("Bar") == 3:
        winnings,win = Bet*200,True
    elif Fruit_Reel.count("Bell") == 3:
        winnings,win = Bet*300,True
    elif Fruit_Reel.count("Seven") == 3:
        
        winnings,win = Bet*1000,True
    # Match 2
    elif Fruit_Reel.count("Blank") == 0:
        if Fruit_Reel.count("Grapes") == 2:
            winnings,win = Bet*2,True
        if Fruit_Reel.count("Banana") == 2:
            winnings,win = Bet*2,True
        elif Fruit_Reel.count("Orange") == 2:
            winnings,win = Bet*3,True
        elif Fruit_Reel.count("Cherry") == 2:
            winnings,win = Bet*4,True
        elif Fruit_Reel.count("Bar") == 2:
            winnings,win = Bet*5,True
        elif Fruit_Reel.count("Bell") == 2:
            winnings,win = Bet*10,True
        elif Fruit_Reel.count("Seven") == 2:
            winnings,win = Bet*20,True
    
        # Match Lucky Seven
        elif Fruit_Reel.count("Seven") == 1:
            winnings, win = Bet*10,True
            
        else:
            winnings, win = Bet*2,True
    if win:    
        
        Player_Money += int(winnings)
    
        # Jackpot 1 in 450 chance of winning
        jackpot_try = random.randrange(1,51,1)
        jackpot_win = random.randrange(1,51,1)
        if  jackpot_try  == jackpot_win:
            messagebox.showinfo("YOU WON!!!!", "CONGRATULATIONS, YOU WON THE JACKPOT!! \n YOU WIN $" + str(Jack_Pot) + ".")
            JackPot_Flag = True
            
        
    
    return Player_Money, Jack_Pot, winnings, Fruit_Reel, Bet, JackPot_Flag

def main():
    #create the window
    root = Tk()
    root.title("Super Slots")
    root.minsize(406, 407)
    root.maxsize(406,407)
    
    #call the MyApp class
    slotMachine = SlotMachine(root)
    root.mainloop()  
    
    
if __name__ == "__main__": main()
