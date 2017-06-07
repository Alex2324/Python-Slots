'''
Slot machine created in Python tKinter.
Created on Nov 28, 2016
@author: Alex
'''
from tkinter import *
import tkinter.messagebox
from winsound import *
import wheel

class Machine:
    def __init__(self):       
        # Create the main window.
        self.main_window = tkinter.Tk()
        
        # set title
        self.main_window.title("Slots")

        # create display images, for slot machine feel
        jackpot = PhotoImage(file="Jackpot.png")
        title = Label(self.main_window, image=jackpot)
        title.grid(row=0, column=0)
        
        # create slot machine image
        display = PhotoImage(file="Slot Machine.png")
        machine = Label(self.main_window, image=display)
        machine.grid(row=1, column=0)
        
        # create submit button and quit button
        self.submit_button = tkinter.Button(self.main_window, \
                                     text='Spin', \
                                     command=self.spin_it)
        self.submit_button.grid(row=5, column=0)

        # create bind key event that allows user to press "Alt and Enter" to submit
        self.main_window.bind("<Alt_L><Return>", lambda event: self.deposit_pot())
        
        self.deposit_label = tkinter.Label(self.main_window, text="Please deposit a pot",
                                                                 font=("Helvetica", 10))
        self.deposit_label.grid(row=2, column=0)
        
        #create register key variable to prevent certain user inputs
        self.vcmd = (self.main_window.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        self.deposit = tkinter.Entry(self.main_window,
                                         width=5, validate='key', validatecommand=self.vcmd)
        self.deposit.grid(row=3, column=0, padx=100)
        self.deposit.focus()
        # create a variable and make it equal a String Variable
        self.dep_value = tkinter.StringVar()
        
        # create submit button and quit button
        self.dep_button = tkinter.Button(self.main_window, \
                                     text='Deposit', \
                                     command=self.deposit_pot)
        self.dep_button.grid(row=5, column=0)
        
        self.coins_won_label = tkinter.Label(self.main_window, text="Coins Won: ",
                                                font=("Helvetica", 12))
        self.coins_won_label.grid(row=6, sticky='w', padx=90)                
        # create a variable and make it equal a String Variable
        self.output_value = tkinter.StringVar()

        self.output_label = tkinter.Label(self.main_window, textvariable=self.output_value,
                                                                 font=("Helvetica", 20),
                                                                 foreground="blue")
        self.output_label.grid(row=6, column=0)
        
        # create a variable and make it equal a String Variable
        self.pot_value = tkinter.StringVar()
        
        self.pot_label = tkinter.Label(self.main_window, text="Pot: ",
                                                font=("Helvetica", 12))
        self.pot_label.grid(row=7, sticky='w', padx=100)
        self.pot_label = tkinter.Label(self.main_window, textvariable=self.pot_value,
                                                                 font=("Helvetica", 12),
                                                                 foreground="gold")
        self.pot_label.grid(row=7, column=0)
        
        #create checkbox to help user turn on or off sound
        self.is_checked = IntVar()
        self.check_sound = Checkbutton(self.main_window, text="Disable sound", onvalue=1, offvalue=0, variable=self.is_checked)
        self.check_sound.grid(row=8, column=0)
        
        # create slot machine sound variable
        self.play = lambda: PlaySound('slotMachine.wav', SND_FILENAME)
        
        # create cash out button
        self.cash_out = tkinter.Button(self.main_window, \
                                     text='Cash out', \
                                     command=self.cash__out)
        self.cash_out.grid(row=8, column=0, sticky='w', padx=10, pady=10)
        
        #create bind event that allows user to double press Enter to cash out
        self.main_window.bind("<Double-Return>", lambda event: self.cash__out())
        
        # create submit button and quit button
        self.rules = tkinter.Button(self.main_window, \
                                     text='Rules', \
                                     command=self.slot_rules)
        self.rules.grid(row=8, column=0, sticky='e', padx=50, pady=10)
        
        #create bind event that allows user to press "Shift and Up" to display rules
        self.main_window.bind("<Shift-Up>", lambda event: self.slot_rules())
        
        self.quit_button = tkinter.Button(self.main_window, \
                                text='Quit', \
                                command=self.main_window.destroy)
        self.quit_button.grid(row=8, column=0, sticky='e', padx=10, pady=10)
        
        #create bind event that allows user to press "Shift and Escape" to exit program
        self.main_window.bind("<Shift-Escape>", lambda event: self.main_window.destroy())
        # enter main loop
        tkinter.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------
    def deposit_pot(self):
        #retrieve main deposit
        self.pot = int(self.deposit.get())
        self.dep_value.set(self.pot)
        
        # remove beginning grids
        self.deposit_label.grid_remove()
        self.deposit.grid_remove()
        self.dep_button.grid_remove()
        
        # now attach regular betting entry
        self.bet_label = tkinter.Label(self.main_window, text="Make a bet",
                                                                 font=("Helvetica", 10))
        self.bet_label.grid(row=2, column=0)
        self.entry = tkinter.Entry(self.main_window,
                                         width=2, validate='key', validatecommand=self.vcmd) 
        self.entry.grid(row=3, column=0, padx=100)
        self.entry.focus()
        # create bind key event that allows user to press "Alt and Enter" to submit
        self.main_window.bind("<Alt_L><Return>", lambda event: self.spin_it())     
#-----------------------------------------------------------------------------------------------------------------------------
    """found this doo-hicky on http://www.tcl.tk/man/tcl8.5/TkCmd/entry.htm#M-validate
    this completely removes the users capability of inputing values not listed in the
    string, I'm still researching what all these arguments entail though"""       
    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                # had to add the next 2 lines in because it would not let me delete every character
                if value_if_allowed == '': 
                    return True
                return False
        else:
            return False
#-----------------------------------------------------------------------------------------------------------------------------        
# begin return number image representation, tried to return an image and then compare but to no avail
    def wheels(self): 
        # create image dictionary
        self.images = {1: PhotoImage(file="bell.png"), 2: PhotoImage(file="grape.png"), 3: PhotoImage(file="cherry.png")}
        # create random number object to determine image to be displayed
        wheel_image = wheel.Wheel()
        
    # First Wheel  
        self.wheel1 = wheel_image.spin()
            
        if self.wheel1 == 1:
            first_image = self.images[1]
        elif self.wheel1 == 2:
            first_image = self.images[2]
        else:
            first_image = self.images[3]
                               
        first_wheel = Label(self.main_window, image=first_image)    
        first_wheel.grid(row=1, sticky="W")
    # Second Wheel
        self.wheel2 = wheel_image.spin() 
                       
        if self.wheel2 == 1:
            second_image = self.images[1]
        elif self.wheel2 == 2:                
            second_image = self.images[2]
        else:
            second_image = self.images[3]
                                
        second_wheel = Label(self.main_window, image=second_image)
        second_wheel.grid(row=1)
    # Third Wheel            
        self.wheel3 = wheel_image.spin() 
                       
        if self.wheel3 == 1:                
            third_image = self.images[1]
        elif self.wheel3 == 2: 
            third_image = self.images[2]
        else:                
            third_image = self.images[3] 
                               
        third_wheel = Label(self.main_window, image=third_image)
        third_wheel.grid(row=1, sticky="E")   
#-----------------------------------------------------------------------------------------------------------------------------
    def spin_it(self):        
        # get user entry
        bet = int(self.entry.get())
        win = 0 

        if bet > self.pot:
                tkinter.messagebox.showerror("Sorry!", "No money") 
                self.main_window.destroy()
        else:
            # make sure bet is between 1 and 4 coins        
            if bet < 1 or bet > 4 or bet is None:
                tkinter.messagebox.showwarning("Hey there", "Cannot have 0 coins or more than 4 coins")            
            # else if 
            else:
                #call wheels to get images
                self.wheels()
                # check if check box is checked        
                if not self.is_checked.get():    
                    # play sound
                    self.play()
                 
                #decrement total by input bet   
                self.pot -= bet
        # create logic to increment pay-out
#-----------------------------------------------------------------------------------------------------------------------------                
                # if all slots are bells
                if self.wheel1 == 1 and self.wheel2 == 1 and self.wheel3 == 1:        
                    win = bet * 10             
                # all slots are grapes
                elif self.wheel1 == 2 and self.wheel2 == 2 and self.wheel3 == 2:    
                    win = bet * 7
                # all slots are cherries
                elif self.wheel1 == 3 and self.wheel2 == 3 and self.wheel3 == 3:
                    win = bet * 5
                # all bell combinations
                elif (self.wheel1 == 1 and self.wheel2 == 1 and self.wheel3 != 1) or \
                                    (self.wheel1 == 1 and self.wheel2 != 1 and self.wheel3 == 1) or \
                                    (self.wheel1 != 1 and self.wheel2 == 1 and self.wheel3 == 1):
                    win = bet * 3
                # all grape combinations                
                elif(self.wheel1 == 2 and self.wheel2 == 2 and self.wheel3 != 2) or \
                                        (self.wheel1 == 2 and self.wheel2 != 2 and self.wheel3 == 2) or \
                                        (self.wheel1 != 2 and self.wheel2 == 2 and self.wheel3 == 2):
                    win = bet * 1
                    
            self.pot += win            
            self.output_value.set(win)
            self.pot_value.set(self.pot)
#create rules display function      
#-----------------------------------------------------------------------------------------------------------------------------           
    def slot_rules(self):
        tkinter.messagebox.showinfo("Rules","No.Combination    Payoff Factor\n\
1    BELL    BELL    BELL    10\n\
2    GRAPE    GRAPE    GRAPE    7\n\
3    CHERRY    CHERRY    CHERRY    5\n\
4    BELL    BELL    ----------    3\n\
5    BELL    ----------    BELL    3\n\
6    ----------    BELL    BELL    3\n\
7    GRAPE    GRAPE    ----------    1\n\
8    GRAPE    ----------    GRAPE    1\n\
9    ----------    GRAPE    GRAPE    1\n\
            All other Combinations    0")
#create cash out method
#-----------------------------------------------------------------------------------------------------------------------------   
    def cash__out(self):
        tkinter.messagebox.showinfo("Thank you!", "Thank you for playing. Please take your check")
        
        reciept = open("winnings.txt", "w")
        reciept.write( "Thank you for playing!\n");
        reciept.write( "Here's your winnings!\n$ ");
        reciept.write(str(self.pot));
        reciept.close()
        
        self.main_window.destroy()

machine = Machine()