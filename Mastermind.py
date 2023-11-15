from random import randint


class Mastermind:
    def __init__(self, colors: int = 6, positions: int = 4):
        self.colors = colors
        self.positions = positions

        self.solution = ''
        for i in range(positions):
            self.solution += str(randint(1, colors))

        self.rounds = 0

    def play(self):
        answer = ''

        print(f"Playing Mastermind with {self.colors} colors and {self.positions} positions")

        while answer != "*" * self.positions:
            right_pos = ''
            right_col = ''
            guess = input("What is your guess?: ")
            print(f'Your guess is {guess}')

            for i in range(len(self.solution)):
                if guess[i] == self.solution[i]:
                    right_pos += '*'
                elif guess[i] in self.solution:
                    right_col += 'o'
            answer = right_pos + right_col
            self.rounds += 1
            print(answer)
            print()

        print(f"You solve it after {self.rounds} rounds")


game = Mastermind()
print(game.solution)
game.play()