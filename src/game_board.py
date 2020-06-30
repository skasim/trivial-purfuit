# TODO *must* reference tic-tac-toe game
#  ref https://github.com/abhishek305/Tic-Tac-Toe-Game-in-python-3-Tkinter/blob/master/my%20tic%20tac%202.py
def board_square_click(playerName, button):
    if button['text'] == ' ':
        button['text'] = playerName
        # TODO add logic here to identify which question to pull up
        # TODO this can be done using the background color
        # print(button['highlightbackground'])
        # print(color_enum.ORANGE.name.lower())
        # print(color_enum.ORANGE.color)

    elif button['text'] != ' ':
        button['text'] = ' '


# TODO create a player object so that it can be passed to command=
def create_game_board(tk_button, root_window, font_type, start_row, sq_dim, color_enum, player1):
    # row 1
    row1_sq1 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.RED.description,
                         height=sq_dim, width=sq_dim, command=lambda: board_square_click(player1.get(), row1_sq1))  # dummy code to show functionality
    row1_sq1.grid(row=start_row, column=1)

    row1_sq2 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.WHITE.description,
                         height=sq_dim, width=sq_dim)
    row1_sq2.grid(row=start_row, column=2)

    row1_sq3 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim)
    row1_sq3.grid(row=start_row, column=3)

    row1_sq4 = tk_button(root_window, text='RED', font=font_type, highlightbackground=color_enum.RED.description,
                         height=sq_dim, width=sq_dim)
    row1_sq4.grid(row=start_row, column=4)

    row1_sq5 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim)
    row1_sq5.grid(row=start_row, column=5)

    row1_sq6 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.WHITE.description,
                         height=sq_dim, width=sq_dim)
    row1_sq6.grid(row=start_row, column=6)

    row1_sq7 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.BLUE.description,
                         height=sq_dim, width=sq_dim)
    row1_sq7.grid(row=start_row, column=7)

    # row 2
    row2_sq1 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.BLUE.description,
                         height=sq_dim, width=sq_dim)
    row2_sq1.grid(row=start_row + 1, column=1)

    row2_sq4 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.WHITE.description,
                         height=sq_dim, width=sq_dim)
    row2_sq4.grid(row=start_row + 1, column=4)

    row2_sq7 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.GREEN.description,
                         height=sq_dim, width=sq_dim)
    row2_sq7.grid(row=start_row + 1, column=7)

    # row 3
    row3_sq1 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim)
    row3_sq1.grid(row=start_row + 2, column=1)

    row3_sq4 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.BLUE.description,
                         height=sq_dim, width=sq_dim)
    row3_sq4.grid(row=start_row + 2, column=4)

    row3_sq7 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim)
    row3_sq7.grid(row=start_row + 2, column=7)

    # row 4 - with center square
    row4_sq1 = tk_button(root_window, text='GREEN', font=font_type, highlightbackground=color_enum.GREEN.description,
                         height=sq_dim,
                         width=sq_dim)  # dummy code to show functionality
    row4_sq1.grid(row=start_row + 3, column=1)

    row4_sq2 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.RED.description,
                         height=sq_dim,
                         width=sq_dim)  # dummy code to show functionality
    row4_sq2.grid(row=start_row + 3, column=2)

    row4_sq3 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.WHITE.description,
                         height=sq_dim, width=sq_dim)
    row4_sq3.grid(row=start_row + 3, column=3)

    row4_sq4 = tk_button(root_window, text='CENTER\nSQUARE', font=font_type,
                         highlightbackground=color_enum.PURPLE.description, height=sq_dim,
                         width=sq_dim)
    row4_sq4.grid(row=start_row + 3, column=4)

    row4_sq5 = tk_button(root_window, text='  ', font=font_type, highlightbackground=color_enum.GREEN.description,
                         height=sq_dim, width=sq_dim)
    row4_sq5.grid(row=start_row + 3, column=5)

    row4_sq6 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.BLUE.description,
                         height=sq_dim, width=sq_dim)
    row4_sq6.grid(row=start_row + 3, column=6)

    row4_sq7 = tk_button(root_window, text='WHITE', font=font_type, highlightbackground=color_enum.WHITE.description,
                         height=sq_dim, width=sq_dim)
    row4_sq7.grid(row=start_row + 3, column=7)

    # row 5
    row5_sq1 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim)
    row5_sq1.grid(row=start_row + 4, column=1)

    row5_sq4 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.RED.description,
                         height=sq_dim, width=sq_dim)
    row5_sq4.grid(row=start_row + 4, column=4)

    row5_sq7 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim)
    row5_sq7.grid(row=start_row + 4, column=7)

    # row 6
    row6_sq1 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.WHITE.description,
                         height=sq_dim, width=sq_dim)
    row6_sq1.grid(row=start_row + 5, column=1)

    row6_sq4 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.GREEN.description,
                         height=sq_dim, width=sq_dim)
    row6_sq4.grid(row=start_row + 5, column=4)

    row6_sq7 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.GREEN.description,
                         height=sq_dim, width=sq_dim)
    row6_sq7.grid(row=start_row + 5, column=7)

    # row 7
    row7_sq1 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.RED.description,
                         height=sq_dim, width=sq_dim)
    row7_sq1.grid(row=start_row + 6, column=1)

    row7_sq2 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.GREEN.description,
                         height=sq_dim, width=sq_dim)
    row7_sq2.grid(row=start_row + 6, column=2)

    row7_sq3 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim)
    row7_sq3.grid(row=start_row + 6, column=3)

    row7_sq4 = tk_button(root_window, text='BLUE', font=font_type, highlightbackground=color_enum.BLUE.description,
                         height=sq_dim, width=sq_dim)
    row7_sq4.grid(row=start_row + 6, column=4)

    row7_sq5 = tk_button(root_window, text='Roll Again', font=font_type,
                         highlightbackground=color_enum.ORANGE.description, height=sq_dim, width=sq_dim)
    row7_sq5.grid(row=start_row + 6, column=5)

    row7_sq6 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.BLUE.description,
                         height=sq_dim, width=sq_dim)
    row7_sq6.grid(row=start_row + 6, column=6)

    row7_sq7 = tk_button(root_window, text=' ', font=font_type, highlightbackground=color_enum.RED.description,
                         height=sq_dim, width=sq_dim)
    row7_sq7.grid(row=start_row + 6, column=7)
