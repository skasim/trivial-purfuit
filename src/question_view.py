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
                                fg=Color.BLACK.description, command=show_answer(question_obj, players, turn, button_text, button_text))
    question_button.grid(row=1, column=0, sticky=tk.W)
    # question_button.configure(command=show_answer())

    return question_label, question_button


def show_answer(question_obj, players, turn, color_type, button_text):
    if question_obj.answer != '':
        verify = messagebox.askyesno("Answer", question_obj.answer + "\nDid you get this correct?")
        if verify:
            if color_type != ' ':
                if color_type == config('CATEGORY1_COLOR') and button_text[0] == '*':
                    players[turn.player_turn].slices.category1 = True
                elif color_type == config('CATEGORY2_COLOR') and button_text[0] == '*':
                    players[turn.player_turn].slices.category2 = True
                elif color_type == config('CATEGORY3_COLOR') and button_text[0] == '*':
                    players[turn.player_turn].slices.category3 = True
                elif color_type == config('CATEGORY4_COLOR') and button_text[0] == '*':
                    players[turn.player_turn].slices.category4 = True
        else:
            turn.increment_player_turn(len(players))
