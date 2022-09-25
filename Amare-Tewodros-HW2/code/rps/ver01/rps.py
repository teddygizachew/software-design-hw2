import random
import emoji

print(emoji.emojize('Win is :thumbs_up:'))
print(emoji.emojize('Loss is :thumbs_down:'))
print("Welcome to Rock Paper Scissor Game")
print("To end the game, enter -> \"q\"")

while True:
    user_move = input("\nEnter move: ")
    if user_move == "r" or user_move == "p" or user_move == "s":
        ai_move = random.choice(["r", "p", "s"])
        if ai_move == user_move:
            print("...TIE...")
        if ai_move == "r" and user_move == "p":
            print(f"{user_move} vs {ai_move} ...{emoji.emojize(':thumbs_up:')}")
        if ai_move == "r" and user_move == "s":
            print(f"{user_move} vs {ai_move} ...{emoji.emojize(':thumbs_down:')}")
        if ai_move == "p" and user_move == "r":
            print(f"{user_move} vs {ai_move} ...{emoji.emojize(':thumbs_down:')}")
        if ai_move == "p" and user_move == "s":
            print(f"{user_move} vs {ai_move} ...{emoji.emojize(':thumbs_up:')}")
        if ai_move == "s" and user_move == "r":
            print(f"{user_move} vs {ai_move} ...{emoji.emojize(':thumbs_up:')}")
        if ai_move == "s" and user_move == "p":
            print(f"{user_move} vs {ai_move} ...{emoji.emojize(':thumbs_down:')}")
    elif user_move == "q":
        print("GAME OVER")
        exit()
    else:
        print("Your input is invalid! Try again")

# Your business logic
# exits when user gives the input 'q'

# Your outputs are copied here
# /usr/bin/python3 /Users/student/Documents/Fall22/ASE_420/Assignments/HW2/Amare-Tewodros-HW2/code/rps/ver01/rps.py
# Win is 👍
# Loss is 👎
# Welcome to Rock Paper Scissor Game
# To end the game, enter -> "q"
#
# Enter move: r
# r vs s ...👍
#
# Enter move: p
# ...TIE...
#
# Enter move: p
# p vs s ...👎
#
# Enter move: s
# s vs r ...👎
#
# Enter move: s
# s vs p ...👍
#
# Enter move: f
# Your input is invalid! Try again
#
# Enter move: q
# GAME OVER
#
# Process finished with exit code 0
