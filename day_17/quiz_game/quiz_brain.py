from typing import List

from day_17.quiz_game.question_model import Question


class QuizBrain:
    question_number: int
    question_list: List[Question]
    score: int

    def __init__(self, question_list: List[Question]):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.__check_answer(current_question.answer, user_answer)

    def __check_answer(self, correct_answer: str, user_answer: str):
        if correct_answer == user_answer:
            print('You got it right!')
            self.score += 1
        else:
            print('Thats wrong')

        print(f'The correct answer was {correct_answer}')
        print(f'Your current score is {self.score}/{self.question_number}')
        print("\n")

    def still_has_questions(self):
        return self.question_number != len(self.question_list)
