import re

'''
The button system for our board game was inspired by abhishek305. “abhishek305/Tic-Tac-Toe-Game-in-Python-3-Tkinter.” 
GitHub, github.com/abhishek305/Tic-Tac-Toe-Game-in-python-3-Tkinter/blob/master/my tic tac 2.py.
'''


def add_player_names_to_player_objects(players, names):
    for key in players:
        this_player = players[key]
        this_name = names[key].get()
        if this_name != '':
            this_player.name = this_name


def board_square_click(players, names, turn, button):
    add_player_names_to_player_objects(players, names)
    board_labels = {'Roll Again', 'CENTER', 'RED', 'WHITE', 'GREEN', 'BLUE'}
    if button['text'] == ' ' and not (button['text'] in board_labels):
        button['text'] = players[turn.player_turn].name
        button['text'] = '{}\n{}'.format(players[turn.player_turn].name,
                                         players[turn.player_turn].slices.get_slices_won())
        # TODO add logic here to identify which question to pull up
        # TODO this can be done using the background color
        # print(button['highlightbackground'])
        # print(color_enum.ORANGE.name.lower())
        # print(color_enum.ORANGE.color)
    elif button['text'] in board_labels:
        button['text'] = '{}{}\n{}'.format('*', button['text'], players[turn.player_turn].name)
    elif button['text'] != ' ' and (button['text'].startswith('*')):
        button['text'] = re.sub(r'^{0}'.format(re.escape('*')), '', button['text']).split('\n')[0]
    elif button['text'] != ' ' and not (button['text'].startswith('*') and button['text'] in board_labels):
        button['text'] = ' '


def create_game_board(tk_button, root_window, font_type, start_row, sq_dim, color_enum, players_dict, names_dict, turn):
    # row 1
    row1_sq1 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.RED.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row1_sq1))
    row1_sq1.grid(row=start_row, column=1)

    row1_sq2 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.WHITE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row1_sq2))
    row1_sq2.grid(row=start_row, column=2)

    row1_sq3 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row1_sq3))
    row1_sq3.grid(row=start_row, column=3)

    row1_sq4 = tk_button(root_window, text='RED', font=font_type, highlightbackground=color_enum.RED.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row1_sq4))
    row1_sq4.grid(row=start_row, column=4)

    row1_sq5 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row1_sq5))
    row1_sq5.grid(row=start_row, column=5)

    row1_sq6 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.WHITE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row1_sq6))
    row1_sq6.grid(row=start_row, column=6)

    row1_sq7 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.BLUE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row1_sq7))
    row1_sq7.grid(row=start_row, column=7)

    # row 2
    row2_sq1 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.BLUE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row2_sq1))
    row2_sq1.grid(row=start_row + 1, column=1)

    row2_sq4 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.WHITE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row2_sq4))
    row2_sq4.grid(row=start_row + 1, column=4)

    row2_sq7 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.GREEN.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row2_sq7))
    row2_sq7.grid(row=start_row + 1, column=7)

    # row 3
    row3_sq1 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row3_sq1))
    row3_sq1.grid(row=start_row + 2, column=1)

    row3_sq4 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.BLUE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row3_sq4))
    row3_sq4.grid(row=start_row + 2, column=4)

    row3_sq7 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row3_sq7))
    row3_sq7.grid(row=start_row + 2, column=7)

    # row 4 - with center square
    row4_sq1 = tk_button(root_window, text='GREEN', font=font_type, highlightbackground=color_enum.GREEN.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row4_sq1))
    row4_sq1.grid(row=start_row + 3, column=1)

    row4_sq2 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.RED.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row4_sq2))
    row4_sq2.grid(row=start_row + 3, column=2)

    row4_sq3 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.WHITE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row4_sq3))
    row4_sq3.grid(row=start_row + 3, column=3)

    row4_sq4 = tk_button(root_window, text='CENTER', font=font_type,
                         highlightbackground=color_enum.PURPLE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row4_sq4))
    row4_sq4.grid(row=start_row + 3, column=4)

    row4_sq5 = tk_button(root_window, text='  ', font=font_type, highlightbackground=color_enum.GREEN.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row4_sq5))
    row4_sq5.grid(row=start_row + 3, column=5)

    row4_sq6 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.BLUE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row4_sq6))
    row4_sq6.grid(row=start_row + 3, column=6)

    row4_sq7 = tk_button(root_window, text='WHITE', font=font_type, highlightbackground=color_enum.WHITE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row4_sq7))
    row4_sq7.grid(row=start_row + 3, column=7)

    # row 5
    row5_sq1 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row5_sq1))
    row5_sq1.grid(row=start_row + 4, column=1)

    row5_sq4 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.RED.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row5_sq4))
    row5_sq4.grid(row=start_row + 4, column=4)

    row5_sq7 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row5_sq7))
    row5_sq7.grid(row=start_row + 4, column=7)

    # row 6
    row6_sq1 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.WHITE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row6_sq1))
    row6_sq1.grid(row=start_row + 5, column=1)

    row6_sq4 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.GREEN.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row6_sq4))
    row6_sq4.grid(row=start_row + 5, column=4)

    row6_sq7 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.GREEN.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row6_sq7))
    row6_sq7.grid(row=start_row + 5, column=7)

    # row 7
    row7_sq1 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.RED.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row7_sq1))
    row7_sq1.grid(row=start_row + 6, column=1)

    row7_sq2 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.GREEN.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row7_sq2))
    row7_sq2.grid(row=start_row + 6, column=2)

    row7_sq3 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row7_sq3))
    row7_sq3.grid(row=start_row + 6, column=3)

    row7_sq4 = tk_button(root_window, text='BLUE', font=font_type, highlightbackground=color_enum.BLUE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row7_sq4))
    row7_sq4.grid(row=start_row + 6, column=4)

    row7_sq5 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row7_sq5))
    row7_sq5.grid(row=start_row + 6, column=5)

    row7_sq6 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.BLUE.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row7_sq6))
    row7_sq6.grid(row=start_row + 6, column=6)

    row7_sq7 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.RED.description,
                         height=sq_dim, width=sq_dim,
                         command=lambda: board_square_click(players_dict, names_dict, turn, row7_sq7))
    row7_sq7.grid(row=start_row + 6, column=7)
