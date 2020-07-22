class Question(object):
    """
    Object representing a question

    :param question: The variable question is used to store the question
    :type question: str

    :param answer: The variable answer is used to store the answer to question
    :type answer: str

    """

    def __init__(self, question='', answer='', color='', category='', was_asked=False):
        self._question = question
        self._answer = answer
        self._color = color
        self._category = category
        self._was_asked = was_asked

    @property
    def question(self):
        """
        Getter method to get question

        :return: question
        :rtype: str
        """
        return self._question

    @property
    def answer(self):
        """
        Getter method to get answer to question

        :return: answer
        :rtype: str
        """
        return self._answer

    @property
    def color(self):
        return self._color

    @property
    def category(self):
        return self._category

    @property
    def was_asked(self):
        return self._was_asked

    @question.setter
    def question(self, question):
        """
        Setter method to set question

        :param question: Represents the question
        """
        self._question = question

    @answer.setter
    def answer(self, answer):
        """
        Setter method to set answer to question

        :param answer: Represents the answer to question
        """
        self._answer = answer

    @color.setter
    def color(self, color):
        self._color = color

    @category.setter
    def category(self, category):
        self._category = category

    @was_asked.setter
    def was_asked(self, was_asked):
        self._was_asked = was_asked
