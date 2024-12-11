class Quiz:
    def __init__(self):
        self.questions={}
        self.user_answers={}
        self.score=0

    def add_question(self,question,answer):
        self.questions[question]=answer

    def remove_question(self,question):
        if question in self.questions:
            del self.questions[question]
        else:
            print(f"Question {question} is not found in the quiz.")

    def take_quiz(self):
        self.user_answers={}
        print("Starting the quiz....")
        for question in self.questions:
            answer=input(f"{question}")
            self.user_answers[question]=answer

    def submit_answer(self,question,answer):
        if question in self.questions:
            self.user_answers[question]=answer
        else:
            print(f"Question {question} not found in the quiz.")

    def calculate_score(self):
        correct_answers=0
        for question, correct_answer in self.questions.items():
            if self.user_answers.get(question)==correct_answer:
                correct_answers+=1
        self.score=correct_answers
        return self.score

    def show_correct_answers(self):
        print("Correct answers:")
        for question,correct_answer in self.questions.items():
            print(f"{question}:{correct_answer}")

quiz=Quiz()

quiz.add_question("What is the capital of France?","Paris")
quiz.add_question("What is 2+2?","4")
quiz.add_question("Who wrote '1984'?","George orwell")

quiz.take_quiz()

score=quiz.calculate_score()
print(f"Your score: {score} out of {len(quiz.questions)}")

quiz.show_correct_answers()
