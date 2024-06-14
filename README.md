# Quiz-Explorer.App

This is a simple quiz management system implemented in Python. It allows users to create quizzes, add questions to quizzes, and provide answers to those questions. Additionally, it enables users to view all quizzes, questions, and answers.

# Getting Started
To get started with the quiz management system, follow the steps below:

1. Clone the repository to your local machine. 
2. Navigate to the project directory. 
3. Run the Python script quiz_management_system.py in your preferred Python environment. pipenv install

# Functionality
## Creating a Quiz
You can create a quiz by providing a title and description. Quizzes are uniquely identified by an ID.

## Adding Questions to a Quiz
For each quiz, you can add multiple-choice questions. Each question can have multiple answers (A, B, C, D) with one correct answer specified.

## Providing Answers
After questions are added, you can provide answers to each question. Answers are associated with the respective question ID.

# Running the code
To view your output on the terminal run this code:

For example ( /bin/python3 /home/documents/Project/Quiz-Explorer.App/cli.py)

 /bin/python3 /(Location of your folder)/(This is where your code is located at)/(This is where your code is located at)/Quiz-Explorer.App/cli.py

# Viewing All Quizzes, Questions, and Answers
The system provides functionality to view all quizzes, questions, and answers. This allows users to see the content of the quizzes and the corresponding answers provided.

# Usage
Here's how you can use the provided functionality:

Run the script quiz_management_system.py.
Follow the prompts to create quizzes, add questions, and provide answers.
Use the viewing functions to see all quizzes, questions, and answers.

## Classes
The system is structured using three main classes:

1. Quiz: Represents a quiz with a title, description, and unique ID.
2. Question: Represents a multiple-choice question with options (A, B, C, D), a correct answer, and associated quiz ID.
3. Answer: Represents an answer to a question with the provided text and associated question ID.

Example Usage
python

Copy code
### Create a new quiz:
create_quiz()

### Add a question to the quiz:
create_question()

### Provide an answer to the question:
create_answer()

### View all quizzes
view_all_quizzes()

### View all questions
view_all_questions()

### View all answers with correct answers
view_all_answers()

## Contributing
Contributions to this project are welcome. Feel free to open issues or submit pull requests to contribute new features, improvements, or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

