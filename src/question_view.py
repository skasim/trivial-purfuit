from src.models.Color import Color
from tkinter import messagebox

def create_question_view(tk, question_frame):
    """
    Method to create the question view

    :param tk: Object representing Tkinter
    :param frame: Tkinter Frame object
    """

    helvetica_20 = tk.font.Font(family='Helvetica', size=20, weight='bold')

    question_label = tk.Label(question_frame, text='What is the name of the first President of the United States of America?',
                              font=helvetica_20, bg=Color.LIGHT_GREEN.description, fg=Color.BLACK.description,
                              wraplength=350, justify='left')
    question_label.grid(row=0, column=0, sticky=tk.E)
    
    def showAnswer():
        messagebox.askyesno("Answer", "The Answer is George Washington. Did you get it correct?")
        
    question_button = tk.Button(question_frame, text='Show Answer', font=helvetica_20, bg=Color.LIGHT_GREEN.description,
                                fg=Color.BLACK.description)
    question_button.grid(row=1, column=0, sticky=tk.W)
