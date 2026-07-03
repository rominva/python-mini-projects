# 1) list of options => rock, paper, scissors
# 2) user choice
# 3) pc choice
# 4) compare choices  => who wins
# rock > scissors
# scissors > paper
# paper > rock
# 5) repeat 3 times


import random

option_list = ["rock", "paper", "scissors"]

pc_score = 0
user_score = 0
time_limit = 3
while time_limit > 0:
    user_choice = input("type your choice; rock, paper or scissors?\n")
    if not user_choice in option_list:
        print("your choice is not accurate! try again.\n")
    else:
        pc_choice = random.choice(option_list)
        print(f"I chose \"{pc_choice}\"")

        if user_choice == pc_choice:
            print(f"we are even! no score for this round. your score => {
                  user_score}\n")
            time_limit -= 1

        if user_choice == "rock":
            if pc_choice == "scissors":
                user_score += 1
                print(f"you got me! your score => {user_score}\n")
                time_limit -= 1
            elif pc_choice == "paper":
                pc_score += 1
                print(f"I won this round. my score =>{pc_score}\n")
                time_limit -= 1

        if user_choice == "scissors":
            if pc_choice == "paper":
                user_score += 1
                print(f"you got me! your score => {user_score}\n")
                time_limit -= 1
            elif pc_choice == "rock":
                pc_score += 1
                print(f"I won this round. my score =>{pc_score}\n")
                time_limit -= 1

        if user_choice == "paper":
            if pc_choice == "rock":
                user_score += 1
                print(f"you got me! your score => {user_score}\n")
                time_limit -= 1
            elif pc_choice == "scissors":
                pc_score += 1
                print(f"I won this round. my score =>{pc_score}\n")
                time_limit -= 1

if pc_score > user_score:
    print(f"you lost! your score: {user_score}, my score: {pc_score}\n")
elif pc_score < user_score:
    print(f"you won! your score: {user_score}, my score: {pc_score}\n")
else:
    print(
        "The end\nWe are even! Your score: {user_score}, My score: {pc_score}\n")
