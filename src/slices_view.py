def create_slices(tk, frame, helvetica_20, Color):
    # capture slices of cake won by a player
    label_p1s = tk.Label(frame, text="Slices 1:", font=helvetica_20, bg=Color.YELLOW.description,
                         fg=Color.BLACK.description,
                         height=1, width=8)
    label_p1s.grid(row=1, column=5, sticky='e')  ## column here tells you where the slices should go

    label_p2s = tk.Label(frame, text="Slices 2:", font=helvetica_20, bg=Color.YELLOW.description,
                         fg=Color.BLACK.description,
                         height=1, width=8)
    label_p2s.grid(row=2, column=5, sticky='e')

    label_p3s = tk.Label(frame, text="Slices 3:", font=helvetica_20, bg=Color.YELLOW.description,
                         fg=Color.BLACK.description,
                         height=1, width=8)
    label_p3s.grid(row=3, column=5, sticky='e')

    label_p4s = tk.Label(frame, text="Slices 4:", font=helvetica_20, bg=Color.YELLOW.description,
                         fg=Color.BLACK.description,
                         height=1, width=8)
    label_p4s.grid(row=4, column=5, sticky='e')