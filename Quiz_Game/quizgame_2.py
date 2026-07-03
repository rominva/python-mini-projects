import random

questions = ["which word means (chair) in Duetch?\n(a)Hallo\n(b)Stuhl\n(c)Straße\n(d)Hemd\n\n",
             "which word means (hello) in Duetch?\n(a)Hallo\n(b)Stuhl\n(c)Straße\n(d)Hemd\n\n",
             "which word means (street) in Duetch?\n(a)Hallo\n(b)Stuhl\n(c)Straße\n(d)Hemd\n\n",
             "which word means (shirt) in Duetch?\n(a)Hallo\n(b)Stuhl\n(c)Straße\n(d)Hemd\n",]


class T_answer:
    def __init__(self, quest, answer):
        self.quest = quest
        self.answer = answer


answers = [T_answer(questions[0], "b"),
           T_answer(questions[1], "a"),
           T_answer(questions[2], "c"),
           T_answer(questions[3], "d")]

s_list = ["No you're Wrong😫 please answer the next question more carefully!\n",
          "Are dump or something!?😒 hehe.. just kiddng😅 or maby not😶\n",
          "if I were you, i would'nt choose that answer😑\n"]

t_list = ["you're so smart! maybe we are relatives😎\n",
          "yesss🥳 that's True!\n",
          "exactly🤩\n"]


print("""\nwelcome to the Quiz test🤗
           please type a, b, c or d as your answer.
           every question has 1 score,
           and if your answer were wrong, you will lose the score💔\n""")

score = 0
for ans in answers:
    user_answer = input(ans.quest)

    if user_answer == ans.answer:
        score += 1
        print(random.choice(t_list))

    elif ans.quest != questions[3]:
        print(random.choice(s_list))

    elif ans.quest == questions[3]:
        print("unfortunately you answerd the last question wrongly😞")

print(f"💙 your score is «{score}» out of «4» 💙")
