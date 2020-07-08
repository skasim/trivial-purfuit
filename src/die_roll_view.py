from src.die_roll import roll_die


def create_die_roll(tk, frame, helvetica_60, helvetica_20, Color):
    # die roll
    die_label = tk.Label(frame, text=' ', font=helvetica_60)
    die_label.grid(row=5, column=2, sticky='e')
    die_button = tk.Button(frame, text='Roll Die', font=helvetica_20, fg=Color.BLACK.description, bg=Color.LIGHT_BLUE.description,
                           command=lambda: roll_die(die_label))
    die_button.grid(row=5, column=1, sticky='e')