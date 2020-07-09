import random
from tkinter.font import Font

'''
The code for using unicode for die faces is from groundhogday321. “groundhogday321/Python-Tkinter-Roll-Dice-Gui.” 
GitHub, github.com/groundhogday321/python-tkinter-roll-dice-gui/blob/master/tkinter roll dice.py.
'''


def roll_die(tk_label):
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    tk_label.configure(text=random.choice(dice))


def create_die_roll(tk, frame, color):
    die_label = tk.Label(frame, text=' ', font=Font(family='Helvetica', size=90, weight='bold'),
                         bg=color.LIGHT_GREEN.description)
    die_label.grid(row=5, column=2, sticky=tk.NE)
    die_button = tk.Button(frame, text='Roll Die', font=Font(family='Helvetica', size=20, weight='bold'),
                           fg=color.BLACK.description, bg=color.LIGHT_GREEN.description,
                           command=lambda: roll_die(die_label))
    die_button.grid(row=5, column=1, sticky=tk.E)
