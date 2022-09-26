import emoji
import random


class Strategy(object):
    def execute(self):
        pass


class Game:
    def __init__(self, count):
        self.count = count

    # def win(self):
    #     print(f"You won ...{emoji.emojize(':thumbs_up:')}")

    def lose(self):
        print(f"You lost ...{emoji.emojize(':thumbs_down:')}")

    def tie(self):
        print("TIE!")

    def increment_games_played(self):
        self.count += 1


class BestTwoOfThreeRPS(Strategy):
    def execute(self):
        print(
            f"{emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')} GAME MODE {emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')}")
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
    def __init__(self, score):
        self.score = score

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

    def get_move(self):
        ai_move = random.choice(["r", "p", "s"])
        return ai_move

    def increment_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def win(self):
        print(f"You won ...{emoji.emojize(':thumbs_up:')}")


class NormalRPS(Strategy):
    def __init__(self, score):
        self.score = score

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

    def get_move(self):
        ai_move = random.choice(["r", "p", "s"])
        return ai_move

    def increment_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def win(self):
        print(f"You won ...{emoji.emojize(':thumbs_up:')}")


class CompeteRPS(Strategy):
    def execute(self):
        print(
            f"{emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')} GAME MODE {emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')}")
        print(f"{emoji.emojize(':video_game:') * 2} Compete Two Strategies {emoji.emojize(':video_game:') * 2}\n")

        game = Game(None)
        count = 0
        no_repeat_strategy = NoRepeatMoveRPS(0)
        normal_strategy = NormalRPS(0)

        prev_move = ""
        while count < 100:
            current_move = no_repeat_strategy.get_move()
            if prev_move != current_move:
                self.play_game(no_repeat_strategy, normal_strategy, game)
                count += 1
                prev_move = current_move

        print(f"Count: {count}")
        print(f"\nNo Repeat = {no_repeat_strategy.get_score()}")
        print(f"\nNormal = {normal_strategy.get_score()}\n")

    def play_game(self, player1, player2, game):
        player1_move = player1.get_move()
        player2_move = player2.get_move()
        if self.valid_move([player1_move, player2_move]):
            if player1_move == player2:
                game.tie()
            if player1_move == "p" and player2_move == "r":
                player1.increment_score()
                print(f"{player1_move} vs {player2_move} -> {player1.get_score()}:{player2.get_score()}")
            if player1_move == "s" and player2_move == "r":
                player2.increment_score()
                print(f"{player1_move} vs {player2_move} -> {player1.get_score()}:{player2.get_score()}")
            if player1_move == "r" and player2_move == "p":
                player2.increment_score()
                print(f"{player1_move} vs {player2_move} -> {player1.get_score()}:{player2.get_score()}")
            if player1_move == "s" and player2_move == "p":
                player1.increment_score()
                print(f"{player1_move} vs {player2_move} -> {player1.get_score()}:{player2.get_score()}")
            if player1_move == "r" and player2_move == "s":
                player1.increment_score()
                print(f"{player1_move} vs {player2_move} -> {player1.get_score()}:{player2.get_score()}")
            if player1_move == "p" and player2_move == "s":
                player2.increment_score()
                print(f"{player1_move} vs {player2_move} -> {player1.get_score()}:{player2.get_score()}")

    def valid_move(self, players_moves):
        valid_moves = ["r", "p", "s"]
        for move in players_moves:
            if move not in valid_moves:
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
        elif strategy == "compete":
            self.set_strategy(CompeteRPS())
        else:
            self.set_strategy(NormalRPS())
        self.strategy.execute()


# Client code
def main():
    c = Context()

    best_two_of_three = "best2of3"
    no_repeat_move = "no_repeat_move"
    normal = "normal"
    compete = "compete"
    # c.choose_game_type(best_two_of_three)
    # c.choose_game_type(no_repeat_move)
    # c.choose_game_type(normal)
    c.choose_game_type(compete)


if __name__ == "__main__":
    main()

# Copy your output here

# -----Best Two Of Three-----
# 🪨 📰 ✂️ GAME MODE 🪨 📰 ✂️
# 🎮🎮 Compete Two Strategies 🎮🎮
#
# p vs r -> 1:0
# r vs s -> 2:0
# s vs p -> 3:0
# p vs s -> 3:1
# p vs s -> 3:2
# p vs r -> 4:2
# s vs r -> 4:3
# r vs p -> 4:4
# s vs p -> 5:4
# r vs s -> 6:4
# s vs r -> 6:5
# p vs s -> 6:6
# s vs r -> 6:7
# r vs p -> 6:8
# r vs s -> 7:8
# s vs p -> 8:8
# s vs r -> 8:9
# s vs p -> 9:9
# s vs r -> 9:10
# r vs p -> 9:11
# s vs p -> 10:11
# r vs s -> 11:11
# s vs r -> 11:12
# r vs p -> 11:13
# r vs p -> 11:14
# p vs r -> 12:14
# s vs p -> 13:14
# r vs p -> 13:15
# s vs p -> 14:15
# p vs s -> 14:16
# p vs r -> 15:16
# s vs r -> 15:17
# r vs s -> 16:17
# r vs s -> 17:17
# p vs s -> 17:18
# r vs s -> 18:18
# p vs s -> 18:19
# r vs p -> 18:20
# r vs p -> 18:21
# r vs s -> 19:21
# p vs r -> 20:21
# s vs p -> 21:21
# r vs s -> 22:21
# p vs s -> 22:22
# p vs r -> 23:22
# s vs p -> 24:22
# s vs r -> 24:23
# r vs p -> 24:24
# p vs s -> 24:25
# r vs p -> 24:26
# s vs r -> 24:27
# p vs r -> 25:27
# r vs p -> 25:28
# p vs r -> 26:28
# p vs r -> 27:28
# r vs p -> 27:29
# s vs p -> 28:29
# s vs p -> 29:29
# s vs r -> 29:30
# p vs s -> 29:31
# Count: 100
#
# No Repeat = 29
#
# Normal = 31