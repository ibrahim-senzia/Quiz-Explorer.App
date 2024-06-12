class Question:
    def __init__(self, id, question, answer_a, answer_b, answer_c, answer_d, correct_answer, quiz_id):
        self.id = id
        self.question = question
        self.answer_a = answer_a
        self.answer_b = answer_b
        self.answer_c = answer_c
        self.answer_d = answer_d
        self.correct_answer = correct_answer
        self.quiz_id = quiz_id
