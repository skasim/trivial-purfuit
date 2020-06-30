import random

# TODO *must* reference below
# ref https://github.com/groundhogday321/python-tkinter-roll-dice-gui/blob/master/tkinter%20roll%20dice.py
def roll_die(tk_label):
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    tk_label.configure(text=random.choice(dice))
