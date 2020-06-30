from tkinter import *
from tkinter.font import Font

from src.die_roll import roll_die
from src.game_board import create_game_board
from src.models.Color import Color
from src.models.Player import Player
from src.models.Turn import Turn

root = Tk()
root.title("Trivial Purfuit by Software Titans")

# set general variables
helvetica_20 = Font(family='Helvetica', size=20, weight='bold')
helvetica_60 = Font(family='Helvetica', size=60, weight='bold')

# Get player names and store them in variables
player1 = StringVar()
player2 = StringVar()
player3 = StringVar()
player4 = StringVar()

player1_name = Entry(root, textvariable=player1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8, sticky='w')
player2_name = Entry(root, textvariable=player2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8, sticky='w')
player3_name = Entry(root, textvariable=player3, bd=5)
player3_name.grid(row=3, column=1, columnspan=8, sticky='w')
player4_name = Entry(root, textvariable=player4, bd=5)
player4_name.grid(row=4, column=1, columnspan=8, sticky='w')

# instantiate players, turn and player objects
turn = Turn()
p1 = Player('player1')
p2 = Player('player2')
p3 = Player('player3')
p4 = Player('player4')

players = {
    1: p1,
    2: p2,
    3: p3,
    4: p4
}

# player name labels
label_p1 = Label(root, text="Player 1:", font=helvetica_20, bg=Color.YELLOW.description, fg=Color.BLACK.description,
                 height=1, width=8)
label_p1.grid(row=1, column=0, sticky='e')

label_p2 = Label(root, text="Player 2:", font=helvetica_20, bg=Color.YELLOW.description, fg=Color.BLACK.description,
                 height=1, width=8)
label_p2.grid(row=2, column=0, sticky='e')

label_p3 = Label(root, text="Player 3:", font=helvetica_20, bg=Color.YELLOW.description, fg=Color.BLACK.description,
                 height=1, width=8)
label_p3.grid(row=3, column=0, sticky='e')

label_p4 = Label(root, text="Player 4:", font=helvetica_20, bg=Color.YELLOW.description, fg=Color.BLACK.description,
                 height=1, width=8)
label_p4.grid(row=4, column=0, sticky='e')

# capture slices of cake won by a player
label_p1s = Label(root, text="Slices:", font=helvetica_20, bg=Color.YELLOW.description, fg=Color.BLACK.description,
                  height=1, width=8)
label_p1s.grid(row=1, column=5, sticky='e')

label_p2s = Label(root, text="Slices:", font=helvetica_20, bg=Color.YELLOW.description, fg=Color.BLACK.description,
                  height=1, width=8)
label_p2s.grid(row=2, column=5, sticky='e')

label_p3s = Label(root, text="Slices:", font=helvetica_20, bg=Color.YELLOW.description, fg=Color.BLACK.description,
                  height=1, width=8)
label_p3s.grid(row=3, column=5, sticky='e')

label_p4s = Label(root, text="Slices:", font=helvetica_20, bg=Color.YELLOW.description, fg=Color.BLACK.description,
                  height=1, width=8)
label_p4s.grid(row=4, column=5, sticky='e')

# die roll
die_label = Label(root, text=' ', font=helvetica_60)
die_label.grid(row=5, column=2, sticky='e')
die_button = Button(root, text='Roll Die', font=helvetica_20, fg=Color.BLACK.description,
                    command=lambda: roll_die(die_label))
die_button.grid(row=5, column=1, sticky='e')

# create the game board
start_row = 11
sq_dim = 7

create_game_board(
    tk_button=Button,
    root_window=root,
    font_type=helvetica_20,
    start_row=start_row,
    sq_dim=sq_dim,
    color_enum=Color,
    players_dict=players,
    turn=turn
)

root.mainloop()
