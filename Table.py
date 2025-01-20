#Importing neccessary libraries
import tkinter as tk 
import random 
import time 

#Creation of the GUI window 
table = tk.Tk()
table.geometry('850x850')
table.title('Python Casino')
table.config(bg= 'green')
table.resizable(False, False)

#Title of the board
tablename = tk.Label(table, text='Python Casino', font=('Vladimir Script', 25) )
tablename.config(bg='green')
tablename.place(x=350, y=5)

#Function that allows for visual bets to be placed and controls the ability to click on and off a bet [set color from blue(bet) to original color]
def place_bet(bets, original_color):
    if bets.cget('bg') =='blue':
        bets.config(bg=original_color)
    
    else: 
        bets.config(bg='blue')

#Create the main bets button layout on board
def bets(text, color, x, y, width, padx):
    bet = tk.Button(table, text=text, font=('Times New Roman', 20), fg='white', bg=color, width=width, padx=padx)
    bet.place(x=x, y=y)

    bet.original_color = color

    bet.config(command=lambda b=bet: place_bet(b, b.original_color))
    return bet

#Creates the canvas window with a grid layout
def grid(picasso, columns, rows, cell_width, cell_height):
    for i in range(columns +1):
        x = i * cell_width
        picasso.create_line(x, 0, x, rows * cell_height, fill = 'white')

    for i in range(rows + 1):
        y = i * cell_height
        picasso.create_line(0, y, columns * cell_width, y, fill = 'white')

#Loops through stored array of even numbers and sets a bet on them 
def even():
    for bet in evenboards:
        bet.config(bg='blue')

#Loops through stored array of odd numbers and sets a bet on them
def odd():
    for bet in oddboards:
        bet.config(bg='blue')

#Loops through both arrays where bets are stored and changes the red bets to blue to signify a bet is placed
def red():
    for bet in evenboards:
        if bet.cget('bg')=='red':
            bet.config(bg='blue')
    for bet in oddboards:
        if bet.cget('bg')=='red':
            bet.config(bg='blue')

#Loops through both arrays where the bets are stored and changes the black bets to blue to signify a bet is placed
def black():
    for bet in evenboards:
        if bet.cget('bg')=='black':
            bet.config(bg='blue')
    for bet in oddboards:
        if bet.cget('bg')=='black':
            bet.config(bg='blue')

#Lines 74-153 create individual functions that are attached to buttons to place larger bets in their designated numerical range based on the looping through both arrays where the bets are stored 
def First12():
    for bet in evenboards:
        try: 
            twelve = int(bet.cget('text'))
            if 1 <= twelve <=12:
                bet.config(bg='blue')
        except ValueError:
            pass
    for bet in oddboards:
        try: 
            twelve = int(bet.cget('text'))
            if 1 <= twelve <=12:
                bet.config(bg='blue')
        except ValueError:
            pass

def Thir24():
    for bet in evenboards:
        try: 
            twelve = int(bet.cget('text'))
            if 13 <= twelve <= 24:
                bet.config(bg='blue')
        except ValueError:
            pass
    for bet in oddboards:
        try: 
            twelve = int(bet.cget('text'))
            if 13 <= twelve <= 24:
                bet.config(bg='blue')
        except ValueError:
            pass

def Twen36():
    for bet in evenboards:
        try: 
            twelve = int(bet.cget('text'))
            if 25 <= twelve <= 36:
                bet.config(bg='blue')
        except ValueError:
            pass
    for bet in oddboards:
        try: 
            twelve = int(bet.cget('text'))
            if 25 <= twelve <= 36:
                bet.config(bg='blue')
        except ValueError:
            pass

def one18():
    for bet in evenboards:
        try: 
            twelve = int(bet.cget('text'))
            if 1 <= twelve <= 18:
                bet.config(bg='blue')
        except ValueError:
            pass
    for bet in oddboards:
        try: 
            twelve = int(bet.cget('text'))
            if 1 <= twelve <= 18:
                bet.config(bg='blue')
        except ValueError:
            pass

def nine36():
    for bet in evenboards:
        try: 
            twelve = int(bet.cget('text'))
            if 19 <= twelve <= 36:
                bet.config(bg='blue')
        except ValueError:
            pass
    for bet in oddboards:
        try: 
            twelve = int(bet.cget('text'))
            if 19 <= twelve <= 36:
                bet.config(bg='blue')
        except ValueError:
            pass  

#Lines 156-199 are buttons that call their respective function and place a large spread of bets based on their designated activity in the game roulette.
One_Twelve = tk.Button(table, text = "1 TO 12", font =("Times New Roman", 20), fg ="white", wraplength = 1, relief ="raised", bd=2, pady =25, command = First12) 
One_Twelve.config(bg='green')
One_Twelve.place(x=359, y=131)
One_Twelve.config(width = 4)

Thirteen_TwentyFour = tk.Button(table, text = "13 TO 24", font =("Times New Roman", 20), fg ="white", wraplength = 1, relief ="raised", bd=2, pady =9, command = Thir24) 
Thirteen_TwentyFour.config(bg='green')
Thirteen_TwentyFour.place(x=359, y=356)
Thirteen_TwentyFour.config(width = 4)

TwentyFive_ThirtySix = tk.Button(table, text = "25 TO 36", font =("Times New Roman", 20), fg ="white", wraplength = 1, relief ="raised", bd=2, pady =9, command = Twen36) 
TwentyFive_ThirtySix.config(bg='green')
TwentyFive_ThirtySix.place(x=359, y=580)
TwentyFive_ThirtySix.config(width = 4)

red_bets = tk.Button(table, text = "RED", font =("Times New Roman", 20), fg ="white", wraplength = 1, relief ="raised", bd=2, pady =25, command = red) 
red_bets.config(bg='red')
red_bets.place(x=288, y=300)
red_bets.config(width = 4)

black_bets = tk.Button(table, text = "BLACK", font =("Times New Roman", 20), fg ="white", wraplength = 1, relief ="raised", bd=2, pady =1, command = black) 
black_bets.config(bg='black')
black_bets.place(x=288, y=464)
black_bets.config(width = 4)

even = tk.Button(table, text = "EVEN", font =("Times New Roman", 20), fg ="white", wraplength = 1, relief ="raised", bd=2, pady =11, command = even) 
even.config(bg='green')
even.place(x=288, y=131)
even.config(width = 4)

odd = tk.Button(table, text = "ODD", font =("Times New Roman", 20), fg ="white", wraplength = 1, relief ="raised", bd=2, pady =27, command = odd) 
odd.config(bg='green')
odd.place(x=288, y=636)
odd.config(width = 4)

one_eighteen = tk.Button(table, text = "1 to 18", font =("Times New Roman", 20), fg ="white", wraplength = 1, relief ="raised", bd=2, pady =80, command = one18) 
one_eighteen.config(bg='green')
one_eighteen.place(x=748, y=131)
one_eighteen.config(width = 4)

nineteen_thirtysix = tk.Button(table, text = "19 to 36", font =("Times New Roman", 20), fg ="white", wraplength = 1, relief ="raised", bd=2, pady =65, command = nine36) 
nineteen_thirtysix.config(bg='green')
nineteen_thirtysix.place(x=748, y=468)
nineteen_thirtysix.config(width = 4)

#Creates the canvas where drawing can occur to create as I did grids for where the main bets were to be placed. 
picasso = tk.Canvas(table, width = 310, height = 669)
picasso.config(bg='green')
picasso.config(borderwidth=1)
picasso.place(x=430, y=130 )

#Calls the function and utilized the 'picasso' canvas to draw a grid. 
grid(picasso, 3, 12, 105, 56)

#Function to loop through both arrays and cancel the bets by setting them back to their original color. 
def reset_buttons():
    for bet in oddboards:
        bet.config(bg=bet.original_color)
    for bet in evenboards:
        bet.config(bg=bet.original_color)

#Button for completing the reset of bets
reset_button = tk.Button(table, text = 'RESET ALL BETS', font = ('Times New Roman', 10), command = reset_buttons)
reset_button.place(x=70, y= 350)

#Array of stored bets on table
evenboards = []
oddboards = []

#Lines 226-264 add the bets into their respective arrays via the append method
oddboards.append(bets('0', 'green', 434, 75, 9,6))
oddboards.append(bets('00', 'green', 590, 75, 9,6))
oddboards.append(bets('1', 'red', 434, 131, 6,False))
evenboards.append(bets('2', 'black', 538, 131,6,False))
oddboards.append(bets('3', 'red', 643, 131,6,False))
evenboards.append(bets('4', 'black', 434, 188,6,False))
oddboards.append(bets('5', 'red', 538, 188,6,False))
evenboards.append(bets('6', 'black', 643, 188,6,False))
oddboards.append(bets('7', 'red', 434, 244,6,False))
evenboards.append(bets('10', 'black', 434, 300,6,False))
oddboards.append(bets('13', 'black', 434, 356,6,False))
evenboards.append(bets('16', 'red', 434, 412,6,False))
oddboards.append(bets('19', 'red', 434, 468,6,False))
evenboards.append(bets('22', 'black', 434, 524,6,False))
oddboards.append(bets('25', 'red', 434, 580,6,False))
evenboards.append(bets('28', 'black', 434, 636,6,False))
oddboards.append(bets('31', 'black', 434, 692,6,False))
evenboards.append(bets('34', 'red', 434, 748,6,False))
evenboards.append(bets('8', 'black', 538, 244,6,False))
oddboards.append(bets('9', 'red', 643, 244,6,False))
oddboards.append(bets('11', 'black', 538, 300,6,False))
evenboards.append(bets('12', 'red', 643, 300,6,False))
evenboards.append(bets('14', 'red', 538, 356,6,False))
oddboards.append(bets('15', 'black', 643, 356,6,False))
oddboards.append(bets('17', 'black', 538, 412,6,False))
evenboards.append(bets('18', 'red', 643, 412,6,False))
evenboards.append(bets('20', 'black', 538, 468,6,False))
oddboards.append(bets('21', 'red', 643, 468,6,False))
oddboards.append(bets('23', 'red', 538, 524,6,False))
evenboards.append(bets('24', 'black', 643, 524,6,False))
evenboards.append(bets('26', 'black', 538, 580,6,False))
oddboards.append(bets('27', 'red', 643, 580,6,False))
oddboards.append(bets('29', 'black', 538, 636,6,False))
evenboards.append(bets('30', 'red', 643, 636,6,False))
oddboards.append(bets('33', 'black', 643, 692,6,False))
evenboards.append(bets('32', 'red', 538, 692,6,False))
oddboards.append(bets('33', 'black', 643, 692,6,False))
oddboards.append(bets('35', 'black', 538, 748,6,False))
evenboards.append(bets('36', 'red', 643, 748,6,False))

#The following is the main roulette method/function in which the game is ran and handled. 

def roulette():
    wheel = oddboards + evenboards

    winningarray = random.choice([oddboards, evenboards])

    winningdraw = random.choice(winningarray)
    print('ROULETTE WHEEL IS SPINNING...')
    #time in this function to create delay between the picking of a winning number and result displayed to the player
    time.sleep(2)
    print("ALL BETS ARE LOCKED IN.")
 
    time.sleep(2)
    print('TAP...TAP...TAP')
    time.sleep(4)
    for bets in wheel:   
        if winningdraw.cget('bg') == 'blue':
            print(f"CONGRATULATIONS WINNER! THE ROULETTE WHEEL SELECTED {winningdraw.cget('text')}")
        else:
            print(f"BETTER LUCK NEXT TIME :( THE ROULETTE WHEEL SELECTED {winningdraw.cget('text')}")
        break
#Button on GUI that calls the roulette function to begin spinning the wheel once bets are locked in. 
SPIN = tk.Button(table, text = 'SPIN', font = ('Times New Roman', 10), command = roulette)
SPIN.place(x=100, y= 400)


table.mainloop()