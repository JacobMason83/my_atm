import tkinter as tk                # importing tkinter as the gui for the app
from tkinter import font  as tkfont #importing all the tkinter functionality
from tkinter import *
from tkinter import font
account_balance = 1000

class My_Atm(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Comic Sans Serif', size=18, weight="bold")
        self.shared_data = {'Balance':tk.IntVar()}
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # This is the page loop for all the pages in the project 
        self.frames = {}
        for F in (Start_Page, Menu_Page, Withdraw_Page, Deposit_Page, Balance_Page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order 
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Start_Page")

    def show_frame(self, page_name):
        #this function shows a page name for the given page, and brings it up 
        frame = self.frames[page_name]
        frame.tkraise()


class Start_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#5203fc")
        self.controller = controller
        

        self.controller.title('Mason Family Bank')
        self.controller.state('zoomed')
        
        heading_label1 = tk.Label(self,
                                 text='Mason Family Banks ATM',
                                 font=('Comic Sans Serif', 50, 'bold'),
                                 fg='white',
                                 bg='#5203fc')
        heading_label1.pack()
        
        space_in_between = tk.Label(self, height=4, bg='#5203fc')
        space_in_between.pack()
        sign_in_label = tk.Label(self,
                                 text='Enter Your Password',
                                 font=('Comic Sans Serif', 15, 'bold'),
                                 fg='white',
                                 bg='#5203fc')
        sign_in_label.pack()
        my_password = tk.IntVar()
        password_entry_box = tk.Entry(self,
                                      text="Enter Your Pin",
                                      textvariable=my_password,
                                      font=('sans serif',13),
                                      width=24)
        password_entry_box.pack(ipady=8)
        
        def password_check():
            if my_password.get() == 123:
                my_password.set('')
                controller.show_frame('Menu_Page')
            else:
                incorrect_password_label["text"]= 'Incorrect Password'
        space_between_input_box = tk.Label(self, height=4, bg='#5203fc')  
        
        space_between_input_box.pack
        check_the_password_button = tk.Button(self,
                                              text='Enter',
                                              command=password_check,
                                              relief='raised',
                                              borderwidth=10,
                                              width=15,
                                              height=2)
        check_the_password_button.pack()
        
        incorrect_password_label = tk.Label(self,
                                            text="",
                                            font=('Comic Sans Serif', 12),
                                            fg='white',
                                            bg='#5203fc',
                                            relief='groove',
                                            borderwidth=4,
                                            height=4,
                                            anchor='n')
        # adding the anchor n which means north so that when the user clicks the enter 
        # #button if incorrect is true it will run this
        incorrect_password_label.pack(fill='both', expand=True)
        
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        

class Menu_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5203fc')
        self.controller = controller
        # label = tk.Label(self, text="Mason Family Bank", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)
        #setting the heading labels for the menu page
        heading_label1 = tk.Label(self,
                                 text='Mason Family Banks ATM',
                                 font=('Comic Sans Serif', 50, 'bold'),
                                 fg='white',
                                 bg='#5203fc')
        heading_label1.pack()
        # making the main menu text 
        main_menu_label = tk.Label(self, 
                                   text='Main Menu',
                                   font=('Comic Sans Serif', 20),
                                   fg='white',
                                   bg='#5203fc')
        main_menu_label.pack()
        #adding this make a selection to make it seem more interactive with the user
        make_a_selection = tk.Label(self,
                                    text="What can we help you with today?",
                                    font=('Comic Sans Serif', 13, 'bold'),
                                    fg='white',
                                    bg='#5203fc')
        make_a_selection.pack(pady=25, fill='x')
        
        button_frame = tk.Frame(self,bg='#4c4d4b')
        button_frame.pack(fill='both',expand=True)
        #adding the function for tkinter to click to the withdraw window on clik
        def withdraw():
            controller.show_frame('Withdraw_Page')
            
        withdraw_button = tk.Button(button_frame,
                                    text='Withdraw', 
                                    command=withdraw,                                   
                                    relief='raised',
                                    borderwidth=10,
                                    width=25,
                                    height=3)
        withdraw_button.grid(column=0, columnspan=2, row=0, padx=5, pady=5)
        #adding the function for tkinter to click to the deposit window on clik
        def deposit():
            controller.show_frame('Deposit_Page')
        # this button is taking in the frame i made above and using it as a grid to make the button and
        # is placing it in the grid at column 0 row 2 with a column span of 2
        deposit_button = tk.Button(button_frame,
                                   text='Deposit',
                                   command=deposit,
                                   relief='raised',
                                   borderwidth=10,
                                   width=25,
                                   height=3)
        deposit_button.grid(column=0,columnspan=2,row=2, padx=5, pady=5)
        #adding the function for tkinter to click to the balance window on clik
        def balance():
            controller.show_frame('Balance_Page')
        balance_button = tk.Button(button_frame,
                                   text='Balance',
                                   command=balance,
                                   relief='raised',
                                   borderwidth=10,
                                   width=25,
                                   height=3)
        balance_button.grid(column=0,columnspan=2,row=4)
        #giving the exit button on the menu page access to the start page so that it will go there on click
        def exit():
            controller.show_frame('Start_Page')
        exit_button = tk.Button(button_frame,
                                   text='Exit',
                                   command=exit,
                                   relief='raised',
                                   borderwidth=10,
                                   width=25,
                                   height=3)
        exit_button.grid(column=0,columnspan=2,row=6,)
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        
        
       

#making the withdraw page class so that when the button is clicked
# it goes to the withdraw page
class Withdraw_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5203fc')
        self.controller = controller
        
        
        #adding the standard heading to the page 
        heading_label1 = tk.Label(self,
                              text='Mason Family Bank ATM',
                                 font=('Comic Sans Serif', 50, 'bold'),
                                 fg='white',
                                 bg='#5203fc')
        heading_label1.pack()
        # need to ask how much they want to withdraw
        amount_to_take_label = tk.Label(self, 
                                   text='How much do you want to withdraw today?',
                                   font=('Comic Sans Serif', 15, 'bold'),
                                   fg='white',
                                   bg='#5203fc')
        amount_to_take_label.pack(side='top', padx=20, pady=20)
        
        #putting in the frame for the withdraw page, so that the buttons are easier to grid
        button_frame = tk.Frame(self,bg='#4c4d4b')
        button_frame.pack(fill='both',expand=True)
        #adding a balance label to the top
        global account_balance #bringing in the global variable so it can be updated, and user can see
        # this is allowing the data to be shared across the pages     
        controller.shared_data['Balance'].set(account_balance)
        #adding a label to be put on the page to be able to be seen when withdrawing
        balance_label = tk.Label(self,
                                 textvariable= controller.shared_data['Balance'],
                                 font=('Comic Sans Serif', 13),
                                 fg='white',
                                 bg='#5203fc', 
                                 anchor='w')
        balance_label.pack(fill='x')
        #making the function for the withdraw method
        def withdraw(amount):
            global account_balance #setting the global balance so that it can be updated
            account_balance -= amount
            controller.shared_data['Balance'].set(account_balance)           
         # adding the button grid of 20 40 60 80 100 other 
        twenty_button = tk.Button(button_frame,
                                  text='$20',
                                  command=lambda: withdraw(20),
                                  relief='raised',
                                  borderwidth=10,
                                  width=25,
                                  height=3)
        twenty_button.grid(row=0, column=0, columnspan=2)
        #40 button
        fourty_button = tk.Button(button_frame,
                                  text='$40',
                                  command=lambda: withdraw(40),
                                  relief='raised',
                                  borderwidth=10,
                                  width=25,
                                  height=3)
        fourty_button.grid(row=1, column=0, columnspan=4)
        #60 button
        sixty_button = tk.Button(button_frame,
                                  text='$60',
                                  command=lambda: withdraw(60),
                                  relief='raised',
                                  borderwidth=10,
                                  width=25,
                                  height=3)
        sixty_button.grid(row=2, column=0, columnspan=2)
        #80 button
        eighty_button = tk.Button(button_frame,
                                  text='$80',
                                  command=lambda: withdraw(80),
                                  relief='raised',
                                  borderwidth=10,
                                  width=25,
                                  height=3)
        eighty_button.grid(row=3, column=0, columnspan=2)
        #100 button
        one_hundred_button = tk.Button(button_frame,
                                  text='$100',
                                  command=lambda: withdraw(100),
                                  relief='raised',
                                  borderwidth=10,
                                  width=25,
                                  height=3)
        one_hundred_button.grid(row=4, column=0, columnspan=2)
        # making the back to menu button
        # other_button = tk.Button(button_frame,
        #                           text='other',
        #                           command=lambda:withdraw(input('Please enter the amount you want to withdraw')),
        #                           relief='raised',
        #                           borderwidth=10,
        #                           width=25,
        #                           height=3)
        # other_button.grid(row=5, column=0, columnspan=2)
        #adding a go back button to the page 
        def go_back():
              controller.show_frame('Menu_Page')
        # adding the button to go back to menu page 
        back_to_menu_button = tk.Button(self,
                                        text='Back to Menu',
                                        command=lambda: go_back(),
                                        fg='white',
                                        bg='#5203fc')
        back_to_menu_button.pack()
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        
#making the deposit page class so that when the button is clicked
# it goes to the deposit page
class Deposit_Page(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5203fc')
        self.controller = controller       
        #adding the heading label to the deposit page 
        heading_label1 = tk.Label(self,
                                 text='Mason Family Bank ATM',
                                 font=('Comic Sans Serif', 50, 'bold'),
                                 fg='white',
                                 bg='#5203fc')
        heading_label1.pack() 
        #need to add a label to ask how much you want to deposit
        need_to_deposit_label = tk.Label(self,
                                          text='How much would you like to deposit?',
                                          font=('Comic Sans Serif', 15, 'bold'),
                                          fg='white',
                                          bg='#5203fc')
        need_to_deposit_label.pack(padx=20, pady=20)
        #need to add the button frame so that it looks like the other pages
        #adding the balance to the page to be seen when depositing
        global account_balance #bringing in the global variable so it can be updated, and user can see
        # this is allowing the data to be shared across the pages     
        controller.shared_data['Balance'].set(account_balance)
        balance_label = tk.Label(self,
                                 textvariable=controller.shared_data['Balance'],
                                 font=('Comic Sans Serif', 13),
                                 fg='white',
                                 bg='#5203fc',
                                 anchor='w')
        balance_label.pack(fill='x')
       
        #adding the function for depositing to the bank 
        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,
                                 textvariable=cash,
                                 font=('Comic Sans Serif', 13),
                                 width=25)
        deposit_entry.pack(ipady=5)

        def deposit_cash(cash):
            global account_balance
            account_balance += int(cash.get())
            controller.shared_data['Balance'].set(account_balance)
            cash.set('')
            controller.show_frame('MenuPage')
            
        deposit_enter_button = tk.Button(self,
                                         text="Enter Your Deposit",
                                         command=lambda: deposit_cash(cash),
                                         relief='raised',
                                         borderwidth=10,
                                         width=15,
                                         height=3)
        deposit_enter_button.pack(ipadx=5, ipady=5)
        #adding a seperation bar to help with the look
        
        # adding a back to menu button on the page 
        def go_back():
              controller.show_frame('Menu_Page')
        back_to_menu_button = tk.Button(self,
                                        text='Back to Menu',
                                        command=lambda: go_back(),
                                        fg='white',
                                        bg='#5203fc')
        back_to_menu_button.pack()
        two_tone_label = tk.Label(self,bg='#4c4d4b')
        two_tone_label.pack(fill='both',expand=True)
        
    #bottom frame of the page to help with seperation 
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
            
          

#making the balance page, so that when the balance button is clicked it goes to the balance page
class Balance_Page(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5203fc')
        self.controller = controller       
    #adding the heading label to the page 
        heading_label1 = tk.Label(self,
                                 text='Mason Family Bank ATM',
                                 font=('Comic Sans Serif', 50, 'bold'),
                                 fg='white',
                                 bg='#5203fc')
        heading_label1.pack()   
        #adding the balance function, button and page details
        global account_balance #bringing in the global variable so it can be updated, and user can see
        # this is allowing the data to be shared across the pages     
        controller.shared_data['Balance'].set(account_balance)
        over_balance_label = tk.Label(self, text='Balance', fg='white',bg='#5203fc',font=('Comic Sans Serif', 30,'bold'),anchor='w')
        over_balance_label.pack()
        balance_label = tk.Label(self,
                                                  textvariable=controller.shared_data['Balance'],
                                                  font=('Comic Sans Serif', 50),
                                                  fg='white',
                                                  bg='#5203fc',
                                                  anchor='w')
        balance_label.pack(fill='x', side='top')
        def go_back():
          controller.show_frame('Menu_Page')
        button_frame = tk.Frame(self, bg='darkblue')
        button_frame.pack(fill='both',expand=True) 
        
        back_to_menu_button = tk.Button(button_frame,
                                        text='Back to Menu',
                                        command=lambda: go_back(),
                                        fg='white',
                                        bg='#5203fc')
        back_to_menu_button.pack()



if __name__ == "__main__":
    app = My_Atm()
    app.mainloop()