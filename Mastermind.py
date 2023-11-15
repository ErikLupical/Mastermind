from random import randint


class Mastermind:
    def __init__(self, colors: int = 6, positions: int = 4):
        self.colors = colors
        self.positions = positions

        self.solution = []
        for i in range(positions):
            self.solution.append(randint(1, colors))

        self.rounds = 0

    def play(self):
        print(f"Playing Mastermind with {self.colors} colors and {self.positions} positions")
        guess = int(input("What is your guess?: "))
        print(f'Your guess is {guess}')
        


game = Mastermind()
print(game.solution)
