class Question(object):
    """
    Object representing a question

    :param question: The variable question is used to store the question
    :type question` str

    :param answer: The variable answer is used to store the answer to question
    :type answer` str

    """

    def __init__(self, question, answer):
        self._question = question
        self._answer = answer

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