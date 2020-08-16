import random
from tkinter.font import Font

from src.models.Color import Color

"""
The code for using unicode for die faces is from groundhogday321. “groundhogday321/Python-Tkinter-Roll-Dice-Gui.” 
GitHub, github.com/groundhogday321/python-tkinter-roll-dice-gui/blob/master/tkinter roll dice.py.
"""

die_button = ''

def roll_die(tk_label):
    """
    Method enables random representing of a die face represented by a unicode string

    :param tk_label: Tkinter Label object
    :return: unicode representation of a die face
    :rtype: str
    """
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    tk_label.configure(text=random.choice(dice))


def create_die_roll(tk, frame):
    """
    Method to create the die roll view

    :param tk: Object representing Tkinter
    :param frame: Tkinter Frame object
    """

    global die_button

    die_label = tk.Label(frame, text=' ', font=Font(family='Helvetica', size=90, weight='bold'),
                         bg=Color.LIGHT_GREEN.description)
    die_label.grid(row=5, column=2, sticky=tk.NE)
    die_button = tk.Button(frame, text='Roll Die', font=Font(family='Helvetica', size=20, weight='bold'),
                           fg=Color.BLACK.description, bg=Color.LIGHT_GREEN.description,
                           command=lambda: roll_die(die_label), state='disabled')
    die_button.grid(row=5, column=1, sticky=tk.E)

def enable_die_roll():
    """
    Method to enable die roll and begin game
    """

    global die_button

    die_button.config(state='normal')


