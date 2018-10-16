class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompt = [
    "What comes after 3 but before 7?\n(a) 4\n(b) 8\n(c) 9\n\n",
    "What comes after 4 but before 8?\n(a) 4\n(b) 5\n(c) 9\n\n",
    "What comes after 5 but before 9?\n(a) 4\n(b) 8\n(c) 9\n\n",
]


questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "b")

]


def run_test(ques):
    score = 0
    for question in ques:
        answer = input(question.prompt)
        if answer == question.prompt:
            score += 1
    print("you got " + str(score) + "/" + str(len(ques)) + " correct")


run_test(questions)
