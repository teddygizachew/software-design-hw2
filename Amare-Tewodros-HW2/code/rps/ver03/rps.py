import emoji
import random


class Strategy(object):
    def execute(self):
        pass


class Game:
    def __init__(self, count):
        self.count = count

    def win(self):
        print(f"You won ...{emoji.emojize(':thumbs_up:')}")

    def lose(self):
        print(f"You lost ...{emoji.emojize(':thumbs_down:')}")

    def tie(self):
        print("TIE!")

    def increment_games_played(self):
        self.count += 1


class BestTwoOfThreeRPS(Strategy):
    def execute(self):
        print(f"{emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')} GAME MODE {emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')}")
        print(f"{emoji.emojize(':video_game:') * 2} Best 2 out of 3 {emoji.emojize(':video_game:') * 2}\n")

        count = 0
        game = Game(count)
        while game.count < 3:
            user_move = input("\nEnter move: ")
            self.play_game(user_move, game)

    def play_game(self, user_move, game):
        if self.valid_move(user_move):
            ai_move = random.choice(["r", "p", "s"])
            if user_move == ai_move:
                game.tie()
                game.increment_games_played()
            if user_move == "p" and ai_move == "r":
                game.win()
                game.increment_games_played()
            if user_move == "s" and ai_move == "r":
                game.lose()
                game.increment_games_played()
            if user_move == "r" and ai_move == "p":
                game.lose()
                game.increment_games_played()
            if user_move == "s" and ai_move == "p":
                game.win()
                game.increment_games_played()
            if user_move == "r" and ai_move == "s":
                game.win()
                game.increment_games_played()
            if user_move == "p" and ai_move == "s":
                game.lose()
                game.increment_games_played()
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


class NoRepeatMoveRPS(Strategy):
    def execute(self):
        print(
            f"{emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')} GAME MODE {emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')}")
        print(f"{emoji.emojize(':video_game:') * 2} No Repeating The Same Move {emoji.emojize(':video_game:') * 2}\n")

        game = Game(None)
        prev_move = ""
        while True:
            current_move = input("\nEnter move: ")
            if prev_move != current_move:
                self.play_game(current_move, game)
            else:
                print("Same move note allowed")
                continue
            prev_move = current_move

    def play_game(self, user_move, game):
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


class NormalRPS(Strategy):
    def execute(self):
        print(
            f"{emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')} GAME MODE {emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')}")
        print(f"{emoji.emojize(':video_game:') * 2} Normal {emoji.emojize(':video_game:') * 2}\n")

        game = Game(None)
        while True:
            user_move = input("\nEnter move: ")
            self.play_game(user_move, game)

    def play_game(self, user_move, game):
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


class Context(object):
    def set_strategy(self, strategy):
        self.strategy = strategy

    def choose_game_type(self, strategy):
        if strategy == "best2of3":  # No money
            self.set_strategy(BestTwoOfThreeRPS())
        elif strategy == "no_repeat_move":
            self.set_strategy(NoRepeatMoveRPS())
        else:
            self.set_strategy(NormalRPS())
        self.strategy.execute()


# Client code
def main():
    c = Context()

    best_two_of_three = "best2of3"
    no_repeat_move = "no_repeat_move"
    normal = "normal"

    # c.choose_game_type(best_two_of_three)
    # c.choose_game_type(no_repeat_move)
    c.choose_game_type(normal)


if __name__ == "__main__":
    main()

# Copy your output here

# -----Best Two Of Three-----

# 🪨 📰 ✂️ GAME MODE 🪨 📰 ✂️
# 🎮🎮 Best 2 out of 3 🎮🎮
#
#
# Enter move: p
# TIE!
#
# Enter move: r
# You won ...👍
#
# Enter move: p
# You lost ...👎
#
# Process finished with exit code 0

# -----No Same Move Allowed-----
# 🪨 📰 ✂️ GAME MODE 🪨 📰 ✂️
# 🎮🎮 No Repeating The Same Move 🎮🎮
#
#
# Enter move: r
# You won ...👍
#
# Enter move: s
# You lost ...👎
#
# Enter move: s
# Same move note allowed
#
# Enter move: p
# You won ...👍
#
# Enter move: s
# TIE!
#
# Enter move: s
# Same move note allowed
#
# Enter move: q
# GAME OVER
#
# Process finished with exit code 0


# -----Normal-----
# 🪨 📰 ✂️ GAME MODE 🪨 📰 ✂️
# 🎮🎮 Normal 🎮🎮
#
#
# Enter move: p
# You won ...👍
#
# Enter move: s
# You won ...👍
#
# Enter move: r
# TIE!
#
# Enter move: s
# You won ...👍
#
# Enter move: p
# You won ...👍
#
# Enter move: qr
# Your input is invalid! Try again
#
# Enter move: q
# GAME OVER
#
# Process finished with exit code 0
