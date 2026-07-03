# MATH QUIZ GAME {2 + 2 = ?}

# my first attempt
# first number random (1,9)
# second number random (1,9)
# operation random
# some questions
# user answer => if ontime & true ==> score

import random
import time

print("🟩 answer the questions as fast as you can.\n🟦 Remember that you have at least 5 seconds for each question!")

score = 0
for x in range(1, 5):
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    oper = random.choice(["+", "-", "/", "x"])

    start_time = time.time()  # timer starts
    user_answer = int(float(input(f"{x}) {num1} {oper} {num2} = ")))
    end_time = time.time()  # timer ends
    delta_time = end_time - start_time    # total time

    if oper == "+":
        true_answer = int(num1 + num2)
    elif oper == "-":
        true_answer = int(num1 - num2)
    elif oper == "x":
        true_answer = int(num1 * num2)
    elif oper == "/":
        true_answer = int(num1 / num2)

    if (user_answer == true_answer) & (delta_time < 5):
        score += 1
        print(f"True! The right answer is:{true_answer}, your score: {score}")

    elif (user_answer == true_answer) & (delta_time > 5):
        print("you ran out of time and can't get a score!")

    else:
        print(f"Wrong! The right answer is {true_answer}")

print(f"\nThe End❤  your total score: {score} out of 5")
print(f"Your time record is about: {round(delta_time)} second")
