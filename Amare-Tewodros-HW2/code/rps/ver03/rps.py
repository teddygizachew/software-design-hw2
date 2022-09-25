import emoji


class Strategy(object):
    def execute(self):
        pass

    def print_header(self):
        print(f"{emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')} GAME MODE {emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')}")

class BestTwoOfThreeRPS(Strategy):
    def execute(self):
        print(f"{emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')} GAME MODE {emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')}")
        print(f"{emoji.emojize(':video_game:') * 2} Best 2 out of 3 {emoji.emojize(':video_game:') * 2}")
        print()


class NoRepeatMoveRPS(Strategy):
    def execute(self):
        print(f"Use Bus - Time (1 hours): Cost ($5)")


class NormalRPS(Strategy):
    def execute(self):
        print(f"{emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')} GAME MODE {emoji.emojize(':rock:')} {emoji.emojize(':newspaper:')} {emoji.emojize(':scissors:')}")
        print(f"{emoji.emojize(':video_game:') * 2} Best 2 out of 3 Mode {emoji.emojize(':video_game:') * 2}")
        print(f"Use Taxi - Time (0.1 hours): Cost ($20)")


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
    # best 2 out of 3
    best_two_of_three = "best2of3"
    no_repeat_move = "no_repeat_move"
    normal = "normal"

    c.make_decision(best_two_of_three)

    c.make_decision(no_repeat_move)

    c.make_decision(normal)


if __name__ == "__main__":
    main()

# Copy your output here
