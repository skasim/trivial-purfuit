import tkinter as tk
from src.die_roll_view import create_die_roll
from src.file_io import load_question_files
from src.game_board_view import create_game_board
from src.models.Color import Color
from src.models.Player import Player
from src.models.Turn import Turn
from src.models.Question import Question
from tkinter.font import Font
from decouple import config

from src.entry_view import create_entry_view
from src.question_view import create_question_view

"""
The code related to organizing canvases within frames and adding scroll bars is from 
user3300676user3300676 15722 gold badges22 silver badges77 bronze badges, et al. “Tkinter Canvas Scrollbar with Grid?” 
Stack Overflow, 1 Nov. 1966, stackoverflow.com/a/49681192/4882806.
"""

ROWS, COLUMNS = 25, 25  # size of grid
DISPLAY_ROWS = 10  # number of rows to display
DISPLAY_COLUMNS = 25  # number of columns to display


class TrivialPurfuit(tk.Tk):
    """
    Main class for the TrivialPurfuit game app
    """

    def __init__(self, title, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        helvetica_20 = Font(family='Helvetica', size=20, weight='bold')

        self.title(title)

        '''
        Create the main frame from the program that encapsulates the main view
        '''
        main_frame = tk.Frame(self, bg=Color.LIGHT_GREEN.description, bd=3, relief=tk.RIDGE)
        main_frame.grid(sticky=tk.NSEW)
        main_frame.columnconfigure(0, weight=1)

        '''
        Create a frame from name entry section of the main view
        '''
        # create a frame for name entry
        frame_entry = tk.Frame(main_frame)
        frame_entry.grid(row=3, column=0, sticky=tk.NW)

        # add canvas to this name entry frame
        canvas_entry = tk.Canvas(frame_entry, bg=Color.LIGHT_GREEN.description, borderwidth=0, highlightthickness=0)
        canvas_entry.grid(row=0, column=0)

        entry_frame = tk.Frame(canvas_entry, bg=Color.LIGHT_GREEN.description, bd=1)

        # Create a frame for question view
        question_view = tk.Frame(main_frame)
        question_view.grid(row=3, column=1, sticky=tk.NW)

        # Add canvas to the question view frame
        question_view_canvas = tk.Canvas(question_view, bg=Color.LIGHT_GREEN.description, borderwidth=0,
                                         highlightthickness=0)
        question_view_canvas.grid(row=0, column=0)

        question_frame = tk.Frame(question_view_canvas, bg=Color.LIGHT_GREEN.description, bd=1)

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

        # instantiate question bank, players, turn and player objects
        question_files = [config('CATEGORY1_FILE'), config('CATEGORY2_FILE'),
                          config('CATEGORY3_FILE'), config('CATEGORY4_FILE')]
        question_bank = load_question_files(question_files)

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

        create_entry_view(
            tk=tk,
            entry_frame=entry_frame,
        )

        canvas_entry.create_window((0, 0), window=entry_frame, anchor=tk.NW)
        entry_frame.update_idletasks()

        question_label = create_question_view(
            tk=tk,
            question_frame=question_frame,
            question_obj=Question(),
            players=players,
            turn=turn,
            button_text=''
        )[0]

        question_button = create_question_view(
            tk=tk,
            question_frame=question_frame,
            question_obj=Question(),
            players=players,
            turn=turn,
            button_text=''
        )[1]

        question_view_canvas.create_window((0, 0), window=question_frame, anchor=tk.NW)
        question_frame.update_idletasks()

        '''
        Create frame for the die roll section of the main view
        '''
        # create frame for die roll
        frame_die_roll = tk.Frame(main_frame)
        frame_die_roll.grid(row=10, column=1, sticky=tk.NW)  # used to be row=4

        # add canvas to this frame
        canvas_die_roll = tk.Canvas(frame_die_roll, bg=Color.LIGHT_GREEN.description, borderwidth=0,
                                    highlightthickness=0)
        canvas_die_roll.grid(row=0, column=0)

        die_roll_frame = tk.Frame(canvas_die_roll, bg=Color.LIGHT_GREEN.description, bd=1)

        create_die_roll(
            tk=tk,
            frame=die_roll_frame
        )

        canvas_die_roll.create_window((0, 0), window=die_roll_frame, anchor=tk.NW)
        die_roll_frame.update_idletasks()

        # create frame for board game and scroll bar
        frame_board_game = tk.Frame(main_frame)
        frame_board_game.grid(row=10, column=0, sticky=tk.NW)

        # add canvas to the frame
        canvas_board_game = tk.Canvas(frame_board_game, bg=Color.WHITE.description)
        canvas_board_game.grid(row=10, column=0)

        # create vertical scroll bar
        vertical_scroll = tk.Scrollbar(frame_board_game, orient=tk.VERTICAL, command=canvas_board_game.yview)
        vertical_scroll.grid(row=10, column=1, sticky=tk.NS)
        canvas_board_game.configure(yscrollcommand=vertical_scroll.set)

        # create horizontal scroll bar
        horizontal_scroll = tk.Scrollbar(frame_board_game, orient=tk.HORIZONTAL, command=canvas_board_game.xview)
        horizontal_scroll.grid(row=1, column=0, sticky=tk.EW)
        canvas_board_game.configure(xscrollcommand=horizontal_scroll.set)

        # create a frame for the board game
        buttons_frame = tk.Frame(canvas_board_game, bg=Color.LIGHT_BLUE.description, bd=1)

        create_game_board(
            tk_button=tk.Button,
            frame=buttons_frame,
            question_label=question_label,
            font_type=helvetica_20,
            start_row=0,
            sq_dim=7,
            names=names,
            players=players,
            turn=turn,
            question_button=question_button,
            question_bank=question_bank
        )

        canvas_board_game.create_window((0, 0), window=buttons_frame, anchor=tk.NW)

        buttons_frame.update_idletasks()
        bbox = canvas_board_game.bbox(tk.ALL)

        # define the scrollable region
        w, h = bbox[2] - bbox[1], bbox[3] - bbox[1]
        dw, dh = int((w / COLUMNS) * DISPLAY_COLUMNS), int((h / ROWS) * DISPLAY_ROWS)
        canvas_board_game.configure(scrollregion=bbox, width=dw, height=dh)


if __name__ == "__main__":
    app = TrivialPurfuit("Trivial Purfuit by Software Titans")
    app.mainloop()
