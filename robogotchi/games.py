import input_handler as handler
from random import randint, choice
from abc import ABC, abstractmethod


class Game(ABC):
    """
    Abstract class of Robogotchi mini-game.
    Implement play() and round_results().
    """

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.active = True
    
    @abstractmethod
    def play(self):
        """Run this method to start the game."""
        pass
    
    @abstractmethod
    def round_results(self):
        """Gather the stats for each round of the game."""
        pass

    def display_stats(self):
        print(f'You won: {self.wins},')
        print(f'The robot won: {self.losses},')
        print(f'Draws: {self.draws}.\n')

    def win(self):
        self.wins += 1
        print('You won!\n')

    def loss(self):
        self.losses += 1
        print('The robot won!\n')

    def draw(self):
        self.draws += 1
        print('It\'s a draw!\n')


class NumberGame(Game):
    """
    Play against Robogotchi by guessing a number in range 0 - 1000000.
    The guesses are compared to a randomly generated number,
    where whoever is closest, wins.
    """

    def play(self):
        """See abstract superclass"""
        while self.active:
            target = randint(0, 1_000_000)
            robo_guess = randint(0, 1_000_000)
            p_guess = handler.game_input(self)
            if p_guess == 'exit':
                self.active = False
                continue
            print(f'The robot entered the number {robo_guess}.')
            print(f'The goal number is {target}')
            self.round_results(p_guess, robo_guess, target)

    def round_results(self, p_guess, robo_guess, target):
        """See abstract superclass"""
        p_diff = abs(target - p_guess)
        robo_diff = abs(target - robo_guess)
        if robo_diff > p_diff:
            self.win()
        elif robo_diff < p_diff:
            self.loss()
        else:
            self.draw()


class RockPaperScissors(Game):
    """
    Play against Robogotchi a classic game of rock-paper-scissors.
    """

    options = ['rock', 'paper', 'scissors']

    def __init__(self):
        super().__init__()

    def play(self):
        """See abstract superclass"""
        while self.active:
            robo_guess = choice(RockPaperScissors.options)
            p_guess = handler.game_input(self)
            if p_guess == 'exit':
                self.active = False
                continue
            print(f'The robot chose {robo_guess}')
            self.round_results(p_guess, robo_guess)

    def round_results(self, p_guess, robo_guess):
        """See abstract superclass"""
        p_guess = RockPaperScissors.options.index(p_guess)
        robo_guess = RockPaperScissors.options.index(robo_guess)
        diff = abs(p_guess - robo_guess)

        if diff == 0:
            self.draw()
        elif p_guess > robo_guess and diff == 1 or \
                p_guess == 0 and diff == 2:
            self.win()
        else:
            self.loss()


def select_game():
    """
    Select a mini-game to play with Robogotchi.
    :return: an instance of a Game object
    """
    option = handler.select_game()
    if option == 1:
        return NumberGame()
    elif option == 2:
        return RockPaperScissors()
    return None
