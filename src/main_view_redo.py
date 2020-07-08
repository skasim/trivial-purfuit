import tkinter as tk
# https://stackoverflow.com/a/49681192/4882806 TODO MUST REFERENCE
from src.game_board import create_game_board
from src.models.Color import Color
from src.models.Player import Player
from src.models.Turn import Turn
from tkinter.font import Font

LABEL_BG = "#ccc"  # Light gray.
ROWS, COLS = 20, 20  # Size of grid.
ROWS_DISP = 15  # Number of rows to display.
COLS_DISP = 20  # Number of columns to display.

class MyApp(tk.Tk):
    def __init__(self, title="Sample App", *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title(title)
        self.configure(background="Gray")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        master_frame = tk.Frame(self, bg="Light Blue", bd=3, relief=tk.RIDGE)
        master_frame.grid(sticky=tk.NSEW)
        master_frame.columnconfigure(0, weight=1)

        # Create a frame for the canvas and scrollbar(s).
        frame2 = tk.Frame(master_frame)
        frame2.grid(row=3, column=0, sticky=tk.NW)

        # Add a canvas in that frame.
        canvas = tk.Canvas(frame2, bg="Yellow")
        canvas.grid(row=0, column=0)

        # Create a vertical scrollbar linked to the canvas.
        vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=1, sticky=tk.NS)
        canvas.configure(yscrollcommand=vsbar.set)

        # Create a horizontal scrollbar linked to the canvas.
        hsbar = tk.Scrollbar(frame2, orient=tk.HORIZONTAL, command=canvas.xview)
        hsbar.grid(row=1, column=0, sticky=tk.EW)
        canvas.configure(xscrollcommand=hsbar.set)

        # Create a frame on the canvas to contain the buttons.
        buttons_frame = tk.Frame(canvas, bg="light blue", bd=2)

        # Add the buttons to the frame.


        turn = Turn()
        p1 = Player('player1')
        p2 = Player('player2')
        p3 = Player('player3')
        p4 = Player('player4')

        names = {
            1: 'joe',
            2: 'larry',
            3: 'curly',
            4: 'moe'
        }

        players = {
            1: p1,
            2: p2,
            3: p3,
            4: p4
        }

        helvetica_20 = Font(family='Helvetica', size=20, weight='bold')

        create_game_board(
            tk_button=tk.Button,
            root_window=buttons_frame,
            font_type=helvetica_20,
            start_row=0,
            sq_dim=7,
            color_enum=Color,
            names_dict=names,
            players_dict=players,
            turn=turn
        )

        # Create canvas window to hold the buttons_frame.
        canvas.create_window((0,0), window=buttons_frame, anchor=tk.NW)

        buttons_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.

        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)


if __name__ == "__main__":
    app = MyApp("Scrollable Canvas")
    app.mainloop()