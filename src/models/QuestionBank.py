import random


class QuestionBank(object):

    def __init__(self,
                 people_questions=[],
                 event_questions=[],
                 places_questions=[],
                 independence_day_questions=[]):
        self._people_questions = people_questions
        self._event_questions = event_questions
        self._places_questions = places_questions
        self._independence_day_questions = independence_day_questions

    @property
    def people_questions(self):
        return self._people_questions

    @property
    def event_questions(self):
        return self._event_questions

    @property
    def places_questions(self):
        return self._places_questions

    @property
    def independence_day_questions(self):
        return self._independence_day_questions

    @people_questions.setter
    def people_questions(self, people_questions):
        self._people_questions = people_questions

    @event_questions.setter
    def event_questions(self, event_questions):
        self._event_questions = event_questions

    @places_questions.setter
    def places_questions(self, places_questions):
        self._places_questions = places_questions

    @independence_day_questions.setter
    def independence_day_questions(self, independence_day_questions):
        self._independence_day_questions = independence_day_questions

    def pick_random_question(self, questions_list):
        select = random.randint(0, len(questions_list)-1)
        print(select)
        question = questions_list[select]

        if not question.was_asked:
            question.was_asked = True
            return question
        else:
            self.pick_random_question(self)
