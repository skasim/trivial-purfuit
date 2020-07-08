from src.die_roll import roll_die


def create_top_view(tk, entry_frame, Color):
    helvetica_60 = tk.font.Font(family='Helvetica', size=60, weight='bold')
    helvetica_20 = tk.font.Font(family='Helvetica', size=20, weight='bold')


    # player name labels
    label_p1 = tk.Label(entry_frame, text="Player 1:", font=helvetica_20, bg=Color.YELLOW.description,
                        fg=Color.BLACK.description,
                        height=1, width=8)
    label_p1.grid(row=1, column=0, sticky='e')

    label_p2 = tk.Label(entry_frame, text="Player 2:", font=helvetica_20, bg=Color.YELLOW.description,
                        fg=Color.BLACK.description,
                        height=1, width=8)
    label_p2.grid(row=2, column=0, sticky='e')

    label_p3 = tk.Label(entry_frame, text="Player 3:", font=helvetica_20, bg=Color.YELLOW.description,
                        fg=Color.BLACK.description,
                        height=1, width=8)
    label_p3.grid(row=3, column=0, sticky='e')

    label_p4 = tk.Label(entry_frame, text="Player 4:", font=helvetica_20, bg=Color.YELLOW.description,
                        fg=Color.BLACK.description,
                        height=1, width=8)
    label_p4.grid(row=4, column=0, sticky='e')

    # capture slices of cake won by a player
    label_p1s = tk.Label(entry_frame, text="Slices:", font=helvetica_20, bg=Color.YELLOW.description,
                         fg=Color.BLACK.description,
                         height=1, width=8)
    label_p1s.grid(row=1, column=5, sticky='e')  ## column here tells you where the slices should go

    label_p2s = tk.Label(entry_frame, text="Slices:", font=helvetica_20, bg=Color.YELLOW.description,
                         fg=Color.BLACK.description,
                         height=1, width=8)
    label_p2s.grid(row=2, column=5, sticky='e')

    label_p3s = tk.Label(entry_frame, text="Slices:", font=helvetica_20, bg=Color.YELLOW.description,
                         fg=Color.BLACK.description,
                         height=1, width=8)
    label_p3s.grid(row=3, column=5, sticky='e')

    label_p4s = tk.Label(entry_frame, text="Slices:", font=helvetica_20, bg=Color.YELLOW.description,
                         fg=Color.BLACK.description,
                         height=1, width=8)
    label_p4s.grid(row=4, column=5, sticky='e')

    # die roll
    die_label = tk.Label(entry_frame, text=' ', font=helvetica_60)
    die_label.grid(row=5, column=2, sticky='e')
    die_button = tk.Button(entry_frame, text='Roll Die', font=helvetica_20, fg=Color.BLACK.description,
                           command=lambda: roll_die(die_label))
    die_button.grid(row=5, column=1, sticky='e')
