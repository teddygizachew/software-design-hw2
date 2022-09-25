"""
install emoji package to display emojis
"""
import random
import emoji


class Game:
    def win(self):
        print(f"You won ...{emoji.emojize(':thumbs_up:')}")

    def lose(self):
        print(f"You lost ...{emoji.emojize(':thumbs_down:')}")

    def tie(self):
        print("TIE!")


class Driver:
    def play_game(self, user_move):
        game = Game()
        if self.valid_move(user_move):
            ai_move = random.choice(["r", "p", "s"])
            if user_move == ai_move:
                game.tie()
            if user_move == "p" and ai_move == "r":
                game.win()
            if user_move == "s" and ai_move == "r":
                game.lose()
            if user_move == "r" and ai_move == "p":
                game.lose()
            if user_move == "s" and ai_move == "p":
                game.win()
            if user_move == "r" and ai_move == "s":
                game.win()
            if user_move == "p" and ai_move == "s":
                game.lose()
        elif user_move == "q":
            print("GAME OVER")
            exit()
        else:
            print("Your input is invalid! Try again")

    def valid_move(self, user_move):
        valid_moves = ["r", "p", "s"]
        if user_move not in valid_moves:
            return False
        return True

    def print_welcome_message(self):
        print(emoji.emojize('Win is :thumbs_up:'))
        print(emoji.emojize('Loss is :thumbs_down:'))
        print("Welcome to Rock Paper Scissor Game")
        print("To end the game, enter -> \"q\"")


# Client code
def main():
    driver = Driver()
    driver.print_welcome_message()
    while True:
        user_move = input("\nEnter move: ")
        driver.play_game(user_move)


if __name__ == "__main__":
    main()

# Copy your output here
# /usr/bin/python3 /Users/student/Documents/Fall22/ASE_420/Assignments/HW2/Amare-Tewodros-HW2/code/rps/ver02/rps.py
# Win is 👍
# Loss is 👎
# Welcome to Rock Paper Scissor Game
# To end the game, enter -> "q"
#
# Enter move: qp
# Your input is invalid! Try again
#
# Enter move: p
# You won ...👍
#
# Enter move: p
# You lost ...👎
#
# Enter move: h
# Your input is invalid! Try again
#
# Enter move: u
# Your input is invalid! Try again
#
# Enter move: s
# You won ...👍
#
# Enter move: q
# GAME OVER
#
# Process finished with exit code 0
