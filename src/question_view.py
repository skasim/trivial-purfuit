from src.models.Color import Color
from tkinter import messagebox
from decouple import config


def create_question_view(tk, question_frame, question_obj, players, turn, button_text):
    """
    Method to create the question view

    :param tk: Object representing Tkinter
    :param question_frame: Tkinter Frame object
    :param question_obj: Question Object
    """

    helvetica_20 = tk.font.Font(family='Helvetica', size=20, weight='bold')

    question_label = tk.Label(question_frame, text=question_obj.question,
                              font=helvetica_20, bg=Color.LIGHT_GREEN.description, fg=Color.BLACK.description,
                              wraplength=200, justify='left')
    question_label.grid(row=0, column=0, sticky=tk.E)

    question_button = tk.Button(question_frame, text='Show Answer', font=helvetica_20, bg=Color.LIGHT_GREEN.description,
                                fg=Color.BLACK.description, command=show_answer(question_obj, players, turn, button_text))
    question_button.grid(row=1, column=0, sticky=tk.W)
    # question_button.configure(command=show_answer())

    return question_label, question_button


def show_answer(question_obj, players, turn, color_type):
    if question_obj.answer != '':
        verify = messagebox.askyesno("Answer", question_obj.answer + "\nDid you get this correct?")
        #TODO
        # check if verify is true. if yes, then check if square is a head square. if true, then add slice to player
        # if answer is false, then move to next player by calling Turn.increment_player_turn()
        if verify:
            if color_type != ' ':
                if color_type == config('CATEGORY1_COLOR'):
                    players[turn.player_turn].slices.category1 = True
                    turn.increment_player_turn(len(players))
                elif color_type == config('CATEGORY2_COLOR'):
                    players[turn.player_turn].slices.category2 = True
                    turn.increment_player_turn(len(players))
                elif color_type == config('CATEGORY3_COLOR'):
                    players[turn.player_turn].slices.category3 = True
                    turn.increment_player_turn(len(players))
                elif color_type == config('CATEGORY4_COLOR'):
                    players[turn.player_turn].slices.category4 = True
                    turn.increment_player_turn(len(players))
        else:
            turn.increment_player_turn(len(players))
