import random


class QuestionBank(object):
    """
    Object representing the bank of questions

    :param category1_questions: The first category of questions set in .env file
    :type category1_questions: str
    :param category2_questions: The second category of questions set in .env file
    :type category2_questions: str
    :param category3_questions: The third category of questions set in .env file
    :type category3_questions: str
    :param category4_questions: The fourth category of questions set in .env file
    :type category4_questions: str
    """

    def __init__(self,
                 category1_questions=[],
                 category2_questions=[],
                 category3_questions=[],
                 category4_questions=[]):
        self._category1_questions = category1_questions
        self._category2_questions = category2_questions
        self._category3_questions = category3_questions
        self._category4_questions = category4_questions

    @property
    def category1_questions(self):
        return self._category1_questions

    @property
    def category2_questions(self):
        return self._category2_questions

    @property
    def category3_questions(self):
        return self._category3_questions

    @property
    def category4_questions(self):
        return self._category4_questions

    @category1_questions.setter
    def category1_questions(self, category1_questions):
        self._category1_questions = category1_questions

    @category2_questions.setter
    def category2_questions(self, category2_questions):
        self._category2_questions = category2_questions

    @category3_questions.setter
    def category3_questions(self, category3_questions):
        self._category3_questions = category3_questions

    @category4_questions.setter
    def category4_questions(self, category4_questions):
        self._category4_questions = category4_questions

    def pick_random_question(self, questions_list):
        select = random.randint(0, len(questions_list) - 1)
        print(select)
        question = questions_list[select]

        if not question.was_asked:
            question.was_asked = True
            return question
        else:
            self.pick_random_question(self)
