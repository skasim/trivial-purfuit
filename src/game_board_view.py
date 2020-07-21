import re
import random

from src.models.Color import Color
from src.models.Question import Question
from src.question_view import showAnswer

"""
The button system for our board game was inspired by abhishek305. “abhishek305/Tic-Tac-Toe-Game-in-Python-3-Tkinter.” 
GitHub, github.com/abhishek305/Tic-Tac-Toe-Game-in-python-3-Tkinter/blob/master/my tic tac 2.py.
"""


def add_player_names_to_player_objects(players, names):
    """
    Method to player names to the Player object. This method is triggered by a lambda function so checks to see if
    player name is updated in the entry view

    :param players: dict of all players with keys being 1, 2, 3, 4
    :type: dict of Player objects
    :param names: dict of player names with keys being 1, 2, 3, 4
    :type: dict of str
    """
    for key in players:
        this_player = players[key]
        this_name = names[key].get()
        if this_name != '':
            this_player.name = this_name


def board_square_click(players, names, turn, button, tk_label, tk_button):
    """
    Method to handle functionality when a board square is clicked

    :param tk_label: Tkinter Label object
    :type: Label
    :param players: dict of all players with keys being 1, 2, 3, 4
    :type: dict of Player objects
    :param names: dict of player names with keys being 1, 2, 3, 4
    :type: dict of str
    :param turn: The current player as represented by Turn object
    :type: Turn object
    :param button: Tkinter Button object
    :type: Button
    :return:
    """
    add_player_names_to_player_objects(players, names)
    board_labels = {'Roll Again', 'CENTER', 'RED', 'WHITE', 'GREEN', 'BLUE'}
    if button['text'] == ' ' and not (button['text'] in board_labels):
        button['text'] = players[turn.player_turn].name
        button['text'] = '{}\n{}'.format(players[turn.player_turn].name,
                                         players[turn.player_turn].slices.get_slices_won())
        display_question(Color.return_color_from_hex(button['highlightbackground']), tk_label, tk_button)

        # TODO add logic here to identify which question to pull up
        # TODO this can be done using the background color
        # print(button['highlightbackground'])
        # print(Color.ORANGE.name.lower())
        # print(Color.ORANGE.color)
    elif button['text'] in board_labels:
        button['text'] = '{}{}\n{}'.format('*', button['text'], players[turn.player_turn].name)
        display_question(Color.return_color_from_hex(button['highlightbackground']), tk_label, tk_button)
    elif button['text'] != ' ' and (button['text'].startswith('*')):
        button['text'] = re.sub(r'^{0}'.format(re.escape('*')), '', button['text']).split('\n')[0]
        display_question(Color, tk_label, tk_button)
    elif button['text'] != ' ' and not (button['text'].startswith('*') and button['text'] in board_labels):
        button['text'] = ' '
        display_question(Color, tk_label, tk_button)


def create_game_board(tk_button, frame, question_label, font_type, start_row, sq_dim, players, names, turn,
                      question_button):
    """
    Method representing the board game view. Each row and button is individually created.

    :param tk_button: Tkinter Button object
    :type: Button
    :param frame: The Frame in which to create the game board
    :type: Frame
    :param question_label: The Label containing the currently displayed question
    :type: Label
    :param font_type: Size and style of font
    :type: Font
    :param start_row: row to start the board game
    :type: int
    :param sq_dim: size of the buttons in the board game
    :type: int
    :param players: dict of all players with keys being 1, 2, 3, 4
    :type: dict of Player objects
    :param names: dict of player names with keys being 1, 2, 3, 4
    :type: dict of str
    :param turn: The current player as represented by Turn object
    :type: Turn object
    """
    # row 1
    row1_sq1 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.RED.description, bg=Color.RED.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row1_sq1, question_label, question_button))
    row1_sq1.grid(row=start_row, column=1)

    row1_sq2 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.WHITE.description, bg=Color.WHITE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row1_sq2, question_label, question_button))
    row1_sq2.grid(row=start_row, column=2)

    row1_sq3 = tk_button(frame, text='Roll Again', font=font_type,
                         highlightbackground=Color.ORANGE.description, bg=Color.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row1_sq3, question_label, question_button))
    row1_sq3.grid(row=start_row, column=3)

    row1_sq4 = tk_button(frame, text='RED', font=font_type, highlightbackground=Color.RED.description, bg=Color.RED.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row1_sq4, question_label, question_button))
    row1_sq4.grid(row=start_row, column=4)

    row1_sq5 = tk_button(frame, text='Roll Again', font=font_type,
                         highlightbackground=Color.ORANGE.description, bg=Color.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row1_sq5, question_label, question_button))
    row1_sq5.grid(row=start_row, column=5)

    row1_sq6 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.WHITE.description, bg=Color.WHITE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row1_sq6, question_label, question_button))
    row1_sq6.grid(row=start_row, column=6)

    row1_sq7 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.BLUE.description, bg=Color.BLUE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row1_sq7, question_label, question_button))
    row1_sq7.grid(row=start_row, column=7)

    # row 2
    row2_sq1 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.BLUE.description, bg=Color.BLUE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row2_sq1, question_label, question_button))
    row2_sq1.grid(row=start_row + 1, column=1)

    row2_sq4 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.WHITE.description, bg=Color.WHITE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row2_sq4, question_label, question_button))
    row2_sq4.grid(row=start_row + 1, column=4)

    row2_sq7 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.GREEN.description, bg=Color.GREEN.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row2_sq7, question_label, question_button))
    row2_sq7.grid(row=start_row + 1, column=7)

    # row 3
    row3_sq1 = tk_button(frame, text='Roll Again', font=font_type,
                         highlightbackground=Color.ORANGE.description, bg=Color.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row3_sq1, question_label, question_button))
    row3_sq1.grid(row=start_row + 2, column=1)

    row3_sq4 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.BLUE.description, bg=Color.BLUE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row3_sq4, question_label, question_button))
    row3_sq4.grid(row=start_row + 2, column=4)

    row3_sq7 = tk_button(frame, text='Roll Again', font=font_type,
                         highlightbackground=Color.ORANGE.description, bg=Color.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row3_sq7, question_label, question_button))
    row3_sq7.grid(row=start_row + 2, column=7)

    # row 4 - with center square
    row4_sq1 = tk_button(frame, text='GREEN', font=font_type, highlightbackground=Color.GREEN.description, bg=Color.GREEN.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row4_sq1, question_label, question_button))
    row4_sq1.grid(row=start_row + 3, column=1)

    row4_sq2 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.RED.description, bg=Color.RED.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row4_sq2, question_label, question_button))
    row4_sq2.grid(row=start_row + 3, column=2)

    row4_sq3 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.WHITE.description, bg=Color.WHITE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row4_sq3, question_label, question_button))
    row4_sq3.grid(row=start_row + 3, column=3)

    row4_sq4 = tk_button(frame, text='CENTER', font=font_type,
                         highlightbackground=Color.PURPLE.description, bg=Color.PURPLE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row4_sq4, question_label, question_button))
    row4_sq4.grid(row=start_row + 3, column=4)

    row4_sq5 = tk_button(frame, text='  ', font=font_type, highlightbackground=Color.GREEN.description, bg=Color.GREEN.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row4_sq5, question_label, question_button))
    row4_sq5.grid(row=start_row + 3, column=5)

    row4_sq6 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.BLUE.description, bg=Color.BLUE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row4_sq6, question_label, question_button))
    row4_sq6.grid(row=start_row + 3, column=6)

    row4_sq7 = tk_button(frame, text='WHITE', font=font_type, highlightbackground=Color.WHITE.description, bg=Color.WHITE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row4_sq7, question_label, question_button))
    row4_sq7.grid(row=start_row + 3, column=7)

    # row 5
    row5_sq1 = tk_button(frame, text='Roll Again', font=font_type,
                         highlightbackground=Color.ORANGE.description, bg=Color.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row5_sq1, question_label, question_button))
    row5_sq1.grid(row=start_row + 4, column=1)

    row5_sq4 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.RED.description, bg=Color.RED.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row5_sq4, question_label, question_button))
    row5_sq4.grid(row=start_row + 4, column=4)

    row5_sq7 = tk_button(frame, text='Roll Again', font=font_type,
                         highlightbackground=Color.ORANGE.description, bg=Color.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row5_sq7, question_label, question_button))
    row5_sq7.grid(row=start_row + 4, column=7)

    # row 6
    row6_sq1 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.WHITE.description, bg=Color.WHITE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row6_sq1, question_label, question_button))
    row6_sq1.grid(row=start_row + 5, column=1)

    row6_sq4 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.GREEN.description, bg=Color.GREEN.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row6_sq4, question_label, question_button))
    row6_sq4.grid(row=start_row + 5, column=4)

    row6_sq7 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.GREEN.description, bg=Color.GREEN.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row6_sq7, question_label, question_button))
    row6_sq7.grid(row=start_row + 5, column=7)

    # row 7
    row7_sq1 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.RED.description, bg=Color.RED.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row7_sq1, question_label, question_button))
    row7_sq1.grid(row=start_row + 6, column=1)

    row7_sq2 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.GREEN.description, bg=Color.GREEN.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row7_sq2, question_label, question_button))
    row7_sq2.grid(row=start_row + 6, column=2)

    row7_sq3 = tk_button(frame, text='Roll Again', font=font_type,
                         highlightbackground=Color.ORANGE.description, bg=Color.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row7_sq3, question_label, question_button))
    row7_sq3.grid(row=start_row + 6, column=3)

    row7_sq4 = tk_button(frame, text='BLUE', font=font_type, highlightbackground=Color.BLUE.description, bg=Color.BLUE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row7_sq4, question_label, question_button))
    row7_sq4.grid(row=start_row + 6, column=4)

    row7_sq5 = tk_button(frame, text='Roll Again', font=font_type,
                         highlightbackground=Color.ORANGE.description, bg=Color.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row7_sq5, question_label, question_button))
    row7_sq5.grid(row=start_row + 6, column=5)

    row7_sq6 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.BLUE.description, bg=Color.BLUE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row7_sq6, question_label, question_button))
    row7_sq6.grid(row=start_row + 6, column=6)

    row7_sq7 = tk_button(frame, text=' ', font=font_type, highlightbackground=Color.RED.description, bg=Color.RED.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players, names, turn, row7_sq7, question_label, question_button))
    row7_sq7.grid(row=start_row + 6, column=7)


def display_question(color_type, tk_label, tk_button):
    """

    :param color_type: Color representing question category
    :param tk_label: Tkinter Label object
    """

    red_questions = 'Red Questions'

    # TODO: Arrange questions and answers into specific categories

    red_questions = [
        Question("Who was the first President of the United States?", "George Washington"),
        Question("Who was the author of the original draft of the Declaration of Independence?", "Thomas Jefferson"),
    ]

    white_questions = [
        Question("What year did the first Continental Congress meet on?", "1774"),
        Question("When was the first draft of the Declaration of Independence signed?", "1776"),
    ]

    blue_questions = [
        Question("What state did Benjamin Franklin first arrive at to seek his fortune?", "Pennsylvania"),
        Question("Where did the first Continental Congress convene?", "Philadelphia"),
    ]

    green_questions = [
        Question("When is Independence Day celebrated in the United States?", "July 4th"),
        Question("What is the most popular form of celebration on Independence Day?", "Having a cookout"),
    ]

    if color_type == Color.RED.color:
        question = random.choice(red_questions)
        tk_label.configure(text=question.question)
        tk_button.configure(command=lambda: showAnswer(question))
    elif color_type == Color.WHITE.color:
        question = random.choice(white_questions)
        tk_label.configure(text=question.question)
        tk_button.configure(command=lambda: showAnswer(question))
    elif color_type == Color.BLUE.color:
        question = random.choice(blue_questions)
        tk_label.configure(text=question.question)
        tk_button.configure(command=lambda: showAnswer(question))
    elif color_type == Color.GREEN.color:
        question = random.choice(green_questions)
        tk_label.configure(text=question.question)
        tk_button.configure(command=lambda: showAnswer(question))
    else:
        tk_label.configure(text=' ')
