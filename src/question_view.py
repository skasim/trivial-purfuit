from src.models.Color import Color
from src.models.Question import Question
from tkinter import messagebox

def create_question_view(tk, question_frame, question_obj):
    """
    Method to create the question view

    :param tk: Object representing Tkinter
    :param question_frame: Tkinter Frame object
    :param question_obj: Question Object
    """

    helvetica_20 = tk.font.Font(family='Helvetica', size=20, weight='bold')

    question_label = tk.Label(question_frame, text=question_obj.question,
                              font=helvetica_20, bg=Color.LIGHT_GREEN.description, fg=Color.BLACK.description,
                              wraplength=350, justify='left')
    question_label.grid(row=0, column=0, sticky=tk.E)
        
    question_button = tk.Button(question_frame, text='Show Answer', font=helvetica_20, bg=Color.LIGHT_GREEN.description,
                                fg=Color.BLACK.description, command=showAnswer(question_obj))
    question_button.grid(row=1, column=0, sticky=tk.W)
    #question_button.configure(command=showAnswer())
    
    return (question_label, question_button)
    
def showAnswer(question_obj):
    if (question_obj.answer != ''):
        messagebox.askyesno("Answer", question_obj.answer + "\nDid you get this correct?")