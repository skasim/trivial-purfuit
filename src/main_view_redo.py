import tkinter as tk
# https://stackoverflow.com/a/49681192/4882806 TODO MUST REFERENCE
from src.die_roll import roll_die
from src.die_roll_view import create_die_roll
from src.game_board import create_game_board
from src.models.Color import Color
from src.models.Player import Player
from src.models.Turn import Turn
from tkinter.font import Font

from src.slices_view import create_slices
from src.top_view import create_top_view

LABEL_BG = "#ccc"  # Light gray.
ROWS, COLS = 25, 25  # Size of grid.
ROWS_DISP = 15  # Number of rows to display.
COLS_DISP = 20  # Number of columns to display.

class MyApp(tk.Tk):
    def __init__(self, title="Sample App", *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        helvetica_20 = Font(family='Helvetica', size=20, weight='bold')
        helvetica_60 = Font(family='Helvetica', size=60, weight='bold')

        self.title(title)
        self.configure(background="Gray")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        master_frame = tk.Frame(self, bg="Light Blue", bd=3, relief=tk.RIDGE)
        master_frame.grid(sticky=tk.NSEW)
        master_frame.columnconfigure(0, weight=1)

        # create a frame for name entry
        frame_entry = tk.Frame(master_frame)
        frame_entry.grid(row=3, column=0, sticky=tk.NW)

        # add canvas to this frame
        canvas_entry = tk.Canvas(frame_entry, bg=Color.LIGHT_BLUE.description, borderwidth=0, highlightthickness=0)
        canvas_entry.grid(row=0, column=0)

        entry_frame = tk.Frame(canvas_entry, bg=Color.LIGHT_BLUE.description, bd=1)

        # Get player names and store them in variables
        player1 = tk.StringVar()
        player2 = tk.StringVar()
        player3 = tk.StringVar()
        player4 = tk.StringVar()

        player1_name = tk.Entry(entry_frame, textvariable=player1, bd=5)
        player1_name.grid(row=1, column=1, columnspan=8, sticky='w')
        player2_name = tk.Entry(entry_frame, textvariable=player2, bd=5)
        player2_name.grid(row=2, column=1, columnspan=8, sticky='w')
        player3_name = tk.Entry(entry_frame, textvariable=player3, bd=5)
        player3_name.grid(row=3, column=1, columnspan=8, sticky='w')
        player4_name = tk.Entry(entry_frame, textvariable=player4, bd=5)
        player4_name.grid(row=4, column=1, columnspan=8, sticky='w')

        # instantiate players, turn and player objects
        turn = Turn()
        p1 = Player('player1')
        p2 = Player('player2')
        p3 = Player('player3')
        p4 = Player('player4')

        names = {
            1: player1,
            2: player2,
            3: player3,
            4: player4
        }

        players = {
            1: p1,
            2: p2,
            3: p3,
            4: p4
        }

        create_top_view(
            tk=tk,
            entry_frame=entry_frame,
            Color=Color,
        )

        canvas_entry.create_window((0, 0), window=entry_frame, anchor=tk.NW)
        entry_frame.update_idletasks()

        # creat slices frame

        frame_slices = tk.Frame(master_frame)
        frame_slices.grid(row=3, column=1, sticky=tk.NW)

        # add canvas to this frame
        canvas_slices = tk.Canvas(frame_slices, bg=Color.LIGHT_BLUE.description, borderwidth=0, highlightthickness=0)
        canvas_slices.grid(row=0, column=0)

        slices_frame = tk.Frame(canvas_slices, bg=Color.LIGHT_BLUE.description, bd=1)

        create_slices(
            tk=tk,
            frame=slices_frame,
            helvetica_20=helvetica_20,
            Color=Color
        )

        canvas_slices.create_window((0,1), window=slices_frame, anchor=tk.NW)
        slices_frame.update_idletasks()

        # create frame for die roll
        frame_die_roll = tk.Frame(master_frame)
        frame_die_roll.grid(row=10, column=1, sticky=tk.NW) #used to be row=4

        # add cavas to this frame
        canvas_die_roll = tk.Canvas(frame_die_roll, bg=Color.LIGHT_BLUE.description, borderwidth=0, highlightthickness=0)
        canvas_die_roll.grid(row=0, column=0)

        die_roll_frame = tk.Frame(canvas_die_roll, bg=Color.LIGHT_BLUE.description, bd=1)

        create_die_roll(
            tk=tk,
            frame=die_roll_frame,
            helvetica_20=helvetica_20,
            helvetica_60=helvetica_60,
            Color=Color
        )

        canvas_die_roll.create_window((0, 0), window=die_roll_frame, anchor=tk.NW)
        die_roll_frame.update_idletasks()

        # Create a frame for the canvas and scrollbar(s).
        frame_board_game = tk.Frame(master_frame)
        frame_board_game.grid(row=10, column=0, sticky=tk.NW)

        # Add a canvas in that frame.
        canvas_board_game = tk.Canvas(frame_board_game, bg="brown")
        canvas_board_game.grid(row=10, column=0)

        # Create a vertical scrollbar linked to the canvas.
        vsbar = tk.Scrollbar(frame_board_game, orient=tk.VERTICAL, command=canvas_board_game.yview)
        vsbar.grid(row=10, column=1, sticky=tk.NS)
        canvas_board_game.configure(yscrollcommand=vsbar.set)

        # Create a horizontal scrollbar linked to the canvas.
        hsbar = tk.Scrollbar(frame_board_game, orient=tk.HORIZONTAL, command=canvas_board_game.xview)
        hsbar.grid(row=1, column=0, sticky=tk.EW)
        canvas_board_game.configure(xscrollcommand=hsbar.set)

        # Create a frame on the canvas to contain the buttons.
        buttons_frame = tk.Frame(canvas_board_game, bg=Color.LIGHT_BLUE.description, bd=1)

        # Add the buttons to the frame.

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
        canvas_board_game.create_window((0, 0), window=buttons_frame, anchor=tk.NW)

        buttons_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas_board_game.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.

        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        w, h = bbox[2] - bbox[1], bbox[3] - bbox[1]
        dw, dh = int((w / COLS) * COLS_DISP), int((h / ROWS) * ROWS_DISP)
        canvas_board_game.configure(scrollregion=bbox, width=dw, height=dh)


if __name__ == "__main__":
    app = MyApp("Scrollable Canvas")
    app.mainloop()
