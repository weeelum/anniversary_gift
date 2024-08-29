"""A class to instantiate various question types."""

from q_a import *
from songs import *

class Question:
    """Used to build game's open-ended questions."""

    def __init__(self, question):
        """Initialize attributes."""
        self.question = question
    
    def display_open_qstn(self):
        """Display open-ended question."""
        question = {
            'question': f'{self.question}'
        }
        print(f"{self.question}")

    def choose_answer(self):
        """Prompt player input for answer choice."""
        ans = input("Choose answer: ")
        return ans
    
    def next_qstn(self):
        """Allow player to advance to next question."""
        confirmation = input("\nEnter 'n' for the next question! ")
        return confirmation
    
    # def check_answer(self):
    #     """Check player answer against correct answer."""

class ChoiceQuestion(Question):
    """Used to build game's multiple choice questions."""

    def __init__(self, question, ans_a, ans_b, ans_c, ans_d):
        """Initialize attributes of the parent class. Then initalize
        attributes specific to multiple choice questions."""
        super().__init__(question)
        self.ans_a = ans_a
        self.ans_b = ans_b
        self.ans_c = ans_c
        self.ans_d = ans_d

    def display_choice_qstn(self):
        """Display open-ended question."""
        question = {
            'question': f'{self.question}',
            'ans_a': f'\t{self.ans_a}',
            'ans_b': f'\t{self.ans_b}',
            'ans_c': f'\t{self.ans_c}',
            'ans_d': f'\t{self.ans_d}'
        }
        for value in question.values():
            print(f"{value}")

class TrueFalse(Question):
    """Used to build game's true/false questions."""

    def __init__(self, question, ans_a, ans_b):
        """Initialize attributes of the parent class. Then initialize
        attributes specific to true/false questions."""
        super().__init__(question)
        self.question = question
        self.ans_a = ans_a
        self.ans_b = ans_b

    def display_TF(self):
        """Display true/false question."""
        question = {
            'question': f'{self.question}',
            'ans_a': f'{self.ans_a}',
            'ans_b': f'{self.ans_b}'
        }
        for value in question.values():
            print(f"{value}")