from src.models.Color import Color
import tkinter as tk

frame = ''

def create_entry_view(tk, entry_frame):
    """
    Method to create the name entry view

    :param tk: Object representing Tkinter
    :param entry_frame: Tkinter Frame object
    """

    global frame

    frame = entry_frame;

    helvetica_20 = tk.font.Font(family='Helvetica', size=20, weight='bold')

    # player name labels
    label_p1 = tk.Label(frame, text="Player 1:", font=helvetica_20, bg=Color.YELLOW.description,
                        fg=Color.BLACK.description,
                        height=1, width=8)
    label_p1.grid(row=1, column=0, sticky='e')

    label_p2 = tk.Label(frame, text="Player 2:", font=helvetica_20, bg=Color.YELLOW.description,
                        fg=Color.BLACK.description,
                        height=1, width=8)
    label_p2.grid(row=2, column=0, sticky='e')

    label_p3 = tk.Label(frame, text="Player 3:", font=helvetica_20, bg=Color.YELLOW.description,
                        fg=Color.BLACK.description,
                        height=1, width=8)
    label_p3.grid(row=3, column=0, sticky='e')

    label_p4 = tk.Label(frame, text="Player 4:", font=helvetica_20, bg=Color.YELLOW.description,
                        fg=Color.BLACK.description,
                        height=1, width=8)
    label_p4.grid(row=4, column=0, sticky='e')

    # current turn label
    label_turn = tk.Label(frame, text="Current Player Turn is:", font=helvetica_20, bg=Color.LIGHT_BLUE.description,
                        fg=Color.BLACK.description,
                        height=1, width=20)
    label_turn.grid(row=6, column=1, sticky='e')

def update_turn(players, turn):
    """
    Method to update which player turn

    :param players: dict of all players with keys being 1, 2, 3, 4
    :type: dict of Player objects
    :param turn: The current player as represented by Turn object
    :type: Turn object
    """
    global frame

    helvetica_20 = tk.font.Font(family='Helvetica', size=20, weight='bold')

    current_turn = tk.Label(frame, text=players[turn.player_turn].name, font=helvetica_20,
                            bg=Color.LIGHT_BLUE.description,
                            fg=Color.BLACK.description,
                            height=1, width=8)
    current_turn.grid(row=6, column=2, sticky='e')




