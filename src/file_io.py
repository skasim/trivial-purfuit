from csv import DictReader
import os
from src.models.Question import Question
from src.models.QuestionBank import QuestionBank
from decouple import config


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
        if file == config('CATEGORY1_FILE'):
            question_bank.category1_questions = load_file(file)
        elif file == config('CATEGORY2_FILE'):
            question_bank.category2_questions = load_file(file)
        elif file == config('CATEGORY3_FILE'):
            question_bank._category3_questions = load_file(file)
        else:
            question_bank.category4_questions = load_file(file)
    return question_bank
