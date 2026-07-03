print("Enter a, b, c or d;")
questions = ["what is 5 + 5?\n(a)10\n(b)25\n(c)1\n(d)0\n\n",
             "what is 5 - 5?\n(a)10\n(b)25\n(c)1\n(d)0\n\n",
             "what is 5 * 5?\n(a)10\n(b)25\n(c)1\n(d)0\n\n",
             "what is 5 / 5?\n(a)10\n(b)25\n(c)1\n(d)0\n\n"]


class Resault:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


# resault1 = Resault(questions[0], "a")
# resault2 = Resault(questions[1], "d")
# resault3 = Resault(questions[2], "b")
# resault4 = Resault(questions[3], "c")

resaults = [Resault(questions[0], "a"),
            Resault(questions[1], "d"),
            Resault(questions[2], "b"),
            Resault(questions[3], "c")]


def take_quiz():
    score = 0
    for quest in resaults:
        user_answer = input(quest.question)
        if user_answer == quest.answer:
            score += 1
    print("your score is:", score)


take_quiz()
