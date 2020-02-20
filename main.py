from random import randint


class NewGame:
    # initiating a new game, by setting all parameters you need and then starting a new iterative round
    def __init__(self, max: int):
        '''
        :param max: the maximum value you want your goal to be
        '''
        self.goal = randint(1, max)
        self.turns = 0

    def start(self):
        print("Guess the number\nby Kolja von der Twer")
        self.new_round()

    # this method checks if the input of the user is equal to, less or higher than the guess.
    # it also increases the number of turns every time call the method
    def new_round(self):
        self.turns += 1
        guess = int(input('Please guess your number:\n'))
        if guess == self.goal:
            print('congratulations, you won the game in ' + str(self.turns) + ' turns!', 'yellow')
        elif guess > self.goal:
            print('The number you entered was higher than the expected number')
            self.new_round()
        else:
            print('The number you entered was lower than the expected number')
            self.new_round()


# setting game as a new game
game = NewGame()
game.start()
