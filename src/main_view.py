from tkinter import *
from tkinter.font import Font

from src.game_board import create_game_board

tk = Tk()
tk.title("Trivial Purfuit by Software Titans")


# set general variables
helvetica_20 = Font(family="Helvetica", size=20, weight="bold")

# TODO convert colors to an Enum
white = '#FFF5C3'
red = '#FF6347'
blue = '#3333FF'
green = '#2C6700'
orange = '#FF9900'
purple = '#CC99CC'
yellow = '#FFFF66'


# Get player names and store them in variables
player1 = StringVar()
player2 = StringVar()
player3 = StringVar()
player4 = StringVar()

player1_name = Entry(tk, textvariable=player1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8, sticky='w')
player2_name = Entry(tk, textvariable=player2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8, sticky='w')
player3_name = Entry(tk, textvariable=player3, bd=5)
player3_name.grid(row=3, column=1, columnspan=8, sticky='w')
player4_name = Entry(tk, textvariable=player4, bd=5)
player4_name.grid(row=4, column=1, columnspan=8, sticky='w')

# player name labels
label = Label(tk, text="Player 1:", font=helvetica_20, bg=yellow, fg='black', height=1, width=8)
label.grid(row=1, column=0, sticky='e')

label = Label(tk, text="Player 2:", font=helvetica_20, bg=yellow, fg='black', height=1, width=8)
label.grid(row=2, column=0, sticky='e')

label = Label(tk, text="Player 3:", font=helvetica_20, bg=yellow, fg='black', height=1, width=8)
label.grid(row=3, column=0, sticky='e')

label = Label(tk, text="Player 4:", font=helvetica_20, bg=yellow, fg='black', height=1, width=8)
label.grid(row=4, column=0, sticky='e')

# capture slices of cake won by a player
label = Label(tk, text="Slices:", font=helvetica_20, bg=yellow, fg='black', height=1, width=8)
label.grid(row=1, column=5, sticky='e')

label = Label(tk, text="Slices:", font=helvetica_20, bg=yellow, fg='black', height=1, width=8)
label.grid(row=2, column=5, sticky='e')

label = Label(tk, text="Slices:", font=helvetica_20, bg=yellow, fg='black', height=1, width=8)
label.grid(row=3, column=5, sticky='e')

label = Label(tk, text="Slices:", font=helvetica_20, bg=yellow, fg='black', height=1, width=8)
label.grid(row=4, column=5, sticky='e')

# create the game board
start_row = 7
sq_dim = 7

create_game_board(Button, tk, helvetica_20, start_row, sq_dim, red, white, orange, blue, green, purple, player1)

tk.mainloop()
