from lib.models.Answer import Answer  # Import Answer class
from lib.models.Question import Question  # Import Question class
from lib.models.Quiz import Quiz  # Import Quiz class
from collections import defaultdict  # Import defaultdict for handling default values

# Default dictionaries to store quizzes, questions, and answers
quizzes = defaultdict(Quiz)
questions = defaultdict(list)
answers = defaultdict(list)

# Global variable to track the current quiz being operated on
current_quiz = None

# Function to create a new quiz
def create_quiz():
    global current_quiz
    title = input("Enter quiz title: ")
    description = input("Enter quiz description: ")
    quiz_id = len(quizzes) + 1
    current_quiz = Quiz(quiz_id, title, description)  # Create a new Quiz object
    quizzes[quiz_id] = current_quiz  # Add the quiz to the quizzes dictionary
    print(f"Quiz {title} created!")

# Function to create a new question for the current quiz
def create_question():
    global current_quiz
    if current_quiz is None:
        print("Please create a quiz first.")
        return
    try:
        question = input("Enter question: ")
        answer_A = input("Enter answer A: ")
        answer_B = input("Enter answer B: ")
        answer_C = input("Enter answer C: ")
        answer_D = input("Enter answer D: ")
        correct_answer = input("Enter correct answer: ")
        # Create a new Question object and add it to the questions dictionary
        question_obj = Question(question, answer_A, answer_B, answer_C, answer_D, correct_answer, current_quiz.id)
        questions[current_quiz.id].append(question_obj)
        print("Question added to the quiz!")
    except ValueError:
        print("Invalid input. Please enter a valid integer for quiz ID.")

# Function to create a new answer for the current question
def create_answer():
    global current_quiz
    if current_quiz is None:
        print("Please create a quiz and a question first.")
        return
    try:
        answer = input("Enter answer: ")
        question_id = current_quiz.id
        answer_id = len(answers[question_id]) + 1
        # Create a new Answer object and add it to the answers dictionary
        answer_obj = Answer(answer_id, answer, question_id)
        answers[question_id].append(answer_obj)
        print(f"Answer {answer} created!")
    except ValueError:
        print("Invalid input. Please enter a valid integer for question ID.")

# Function to view all quizzes
def view_all_quizzes():
    print("List of Quizzes:")
    for quiz_id, quiz in quizzes.items():
        print(f"Quiz ID: {quiz_id} - Title: {quiz.title}")

# Function to view all questions and their answers
def view_all_questions():
    print("List of Questions:")
    for quiz_id, quiz_questions in questions.items():
        print(f"Quiz ID: {quiz_id}")
        for question in quiz_questions:
            print(question.question)
            print("Answers:")
            for answer_obj in answers[question.quiz_id]:
                print(f"{answer_obj.id}. {answer_obj.answer}")
            print("-----------------------------")

# Function to view all answers
def view_all_answers():
    print("List of Answers:")
    for question_id, question_answers in answers.items():
        print(f"Question ID: {question_id}")
        for answer in question_answers:
            print(f"Answer: {answer.answer}")
        # Get the correct answer from the corresponding question
        correct_answer = next((q.correct_answer for q in questions[question_id]), None)
        if correct_answer:
            print(f"Correct Answer: {correct_answer}")
        print()

# Main menu function to handle user interaction
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Create Quiz")
        print("2. Create Question")
        print("3. Create Answer")
        print("4. View All Quizzes")
        print("5. View All Questions")
        print("6. View All Answers")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_quiz()
        elif choice == '2':
            create_question()
        elif choice == '3':
            create_answer()
        elif choice == '4':
            view_all_quizzes()
        elif choice == '5':
            view_all_questions()
        elif choice == '6':
            view_all_answers()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()  # Run the main menu function if the script is executed directly
