import emoji


class Strategy(object):
    def execute(self):
        pass


class BestTwoOfThreeRPS(Strategy):
    def execute(self):
        print(
            f"{emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')} GAME MODE {emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')}")
        print(f"{emoji.emojize(':video_game:') * 2} Best 2 out of 3 {emoji.emojize(':video_game:') * 2}")
        print()


class NoRepeatMoveRPS(Strategy):
    def execute(self):
        print(
            f"{emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')} GAME MODE {emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')}")
        print(f"{emoji.emojize(':video_game:') * 2} No Repeating The Same Move {emoji.emojize(':video_game:') * 2}")
        print()


class NormalRPS(Strategy):
    def execute(self):
        print(
            f"{emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')} GAME MODE {emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')}")
        print(f"{emoji.emojize(':video_game:') * 2} Normal {emoji.emojize(':video_game:') * 2}")
        print()


class Context(object):
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def make_decision(self, strategy):
        if strategy == "best2of3":  # No money
            self.set_strategy(BestTwoOfThreeRPS())
        elif strategy < "no_repeat_move":
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

    c.make_decision(best_two_of_three)
    c.make_decision(no_repeat_move)
    c.make_decision(normal)


if __name__ == "__main__":
    main()

# Copy your output here
