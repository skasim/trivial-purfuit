from csv import DictReader
import os
#TODO https://thispointer.com/python-read-a-csv-file-line-by-line-with-or-without-header/#:~:text=Read%20csv%20file%20line%20by,cell%20values%20for%20that%20row.&text=It%20iterates%20over%20all%20the%20rows%20of%20students,-.
from src.models.Question import Question
from src.models.QuestionBank import QuestionBank


def load_file(filename):
    questions = []
    with open(os.path.abspath(filename), 'r', encoding='utf-8-sig') as f:
        file = DictReader(f)
        for row in file:
            question = Question(
                question=row['question'],
                answer=row['answer'],
                color=row['color'],
                category=row['category']
            )
            questions.append(question)
        return questions


def load_question_files(question_files):
    question_bank = QuestionBank()
    for file in question_files:
        if file == 'question_files/people.csv':
            question_bank.people_questions = load_file(file)
        elif file == 'question_files/events.csv':
            question_bank.event_questions = load_file(file)
        elif file == 'question_files/places.csv':
            question_bank.places_questions = load_file(file)
        else:
            question_bank.independence_day_questions = load_file(file)
    return question_bank




