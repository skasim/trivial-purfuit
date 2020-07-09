def create_entry_view(tk, entry_frame, color):
    helvetica_20 = tk.font.Font(family='Helvetica', size=20, weight='bold')

    # player name labels
    label_p1 = tk.Label(entry_frame, text="Player 1:", font=helvetica_20, bg=color.YELLOW.description,
                        fg=color.BLACK.description,
                        height=1, width=8)
    label_p1.grid(row=1, column=0, sticky='e')

    label_p2 = tk.Label(entry_frame, text="Player 2:", font=helvetica_20, bg=color.YELLOW.description,
                        fg=color.BLACK.description,
                        height=1, width=8)
    label_p2.grid(row=2, column=0, sticky='e')

    label_p3 = tk.Label(entry_frame, text="Player 3:", font=helvetica_20, bg=color.YELLOW.description,
                        fg=color.BLACK.description,
                        height=1, width=8)
    label_p3.grid(row=3, column=0, sticky='e')

    label_p4 = tk.Label(entry_frame, text="Player 4:", font=helvetica_20, bg=color.YELLOW.description,
                        fg=color.BLACK.description,
                        height=1, width=8)
    label_p4.grid(row=4, column=0, sticky='e')
