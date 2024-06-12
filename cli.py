from lib.models.Answer import Answer
from lib.models.Question import Question
from lib.models.Quiz import Quiz
from collections import defaultdict

quizzes = defaultdict(list)
questions = defaultdict(list)
answers = defaultdict(list)

def create_quiz():
    title = input("Enter quiz title: ")
    description = input("Enter quiz description: ")
    quiz_id = len(quizzes) + 1
    quiz = Quiz(quiz_id, title, description)
    quizzes[quiz_id] = quiz
    print(f"Quiz {title} created!")

def create_question():
    question = input("Enter question: ")
    answer_a = input("Enter answer A: ")
    answer_b = input("Enter answer B: ")
    answer_c = input("Enter answer C: ")
    answer_d = input("Enter answer D: ")
    correct_answer = input("Enter correct answer: ")
    quiz_id = int(input("Enter quiz ID: "))
    question_id = len(questions[quiz_id]) + 1
    question_obj = Question(question_id, question, answer_a, answer_b, answer_c, answer_d, correct_answer, quiz_id)
    questions[quiz_id].append(question_obj)
    print(f"Question {question} created!")

def create_answer():
    answer = input("Enter answer: ")
    question_id = int(input("Enter question ID: "))
    answer_id = len(answers[question_id]) + 1
    answer_obj = Answer(answer_id, answer, question_id)
    answers[question_id].append(answer_obj)
    print(f"Answer {answer} created!")

