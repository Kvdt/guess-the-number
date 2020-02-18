import config
from termcolor import colored

class NewGame:
    print(config.welcomemsg)

    # initiating a new game, by setting all parameters you need and then starting a new iterative round
    def __init__(self):
        self.max = config.max
        self.goal = config.randint(1, self.max)
        self.turns = 0

    def start(self):
        self.new_round()

    # this method checks if the input of the user is equal to, less or higher than the guess.
    # it also increases the number of turns every time you don't get the right number
    def new_round(self):
        guess = int(input('Please guess your number:\n'))
        # this prevents the script from saying 0 turns
        if guess == self.goal:
            self.turns += 1
            print(colored('congratulations, you won the game in ' + str(self.turns) + ' turns!', 'yellow'))
        elif guess > self.goal:
            print('The number you entered was higher than the expected number')
            self.turns += 1
            self.new_round()
        elif guess < self.goal:
            print('The number you entered was lower than the expected number')
            self.turns += 1
            self.new_round()


# setting game as a new game
game = NewGame()
game.start()
