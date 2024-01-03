from typing import List

import day_17.quiz_game.data as data
from day_17.quiz_game.question_model import Question
from day_17.quiz_game.quiz_brain import QuizBrain


def convert_questions_to_array():
    converted_data: List[Question] = []
    for question in data.question_data:
        converted_data.append(Question(question['question'], question['correct_answer']))

    return converted_data


question_bank = convert_questions_to_array()

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print('You have completed the quiz')
print(f"Your final score is {quiz_brain.score}/{len(quiz_brain.question_list)}")
