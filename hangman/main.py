import string
import hangman_ascii as hascii
from random import choice
from hangman import Hangman


class HangmanGame:
    """
    Initiate a hangman game
    
    :ivar hangman: Class Hangman
    :ivar active: The state of the game
    """

    def __init__(self):
        print(hascii.logo)
        self.hangman = Hangman(self.random_word())
        self.active = True
    
    @staticmethod
    def random_word():
        """
        Select a random word from a text file.
        :return: a lower-case word
        """
        with open('hangman_words.csv', 'r') as wordlist:
            word = choice(wordlist.read().split(','))
        return word
    
    def play(self):
        """
        Run this method to start the game.
        """
        while self.active:
            while self.active:
                print(self.hangman)
                print(f'\nNumber of lives left: {self.hangman.lives}\n')
                # user plays
                letter = input('Input a letter: ').lower()
                if self.is_valid_letter(letter):
                    self.hangman.guess(letter)
                    # check winning condition
                    if self.hangman.is_saved():
                        print(hascii.figure['saved'])
                        print('\nYou survived!')
                        self.active = False
                    # check losing condition
                    elif self.hangman.is_hanged():
                        print(hascii.figure[1])
                        print('\nYou are hanged!')
                        print(f'The word was {self.hangman.word}')
                        self.active = False
                print()
            self.active = self.replay()
        print('\nThank you for playing!')
        print(hascii.logo)
    
    @staticmethod
    def is_valid_letter(c):
        """
        Check if character c is a single English lowercase letter
        :param c: a character
        :return True if character is valid, else False
        """
        if len(c) != 1:
            print('You should input a single letter')
            return False
        if c not in string.ascii_letters:
            print('You did not input a valid English letter')
            return False
        return True

    def replay(self):
        """
        Ask the user if they want to replay hangman.
        :return: True if affirmative, else False
        """
        while True:
            user_input = input('\nWould you like to [R]eplay or [Q]uit?: ')
            if user_input[0].lower() == 'r':
                self.hangman = Hangman(self.random_word())  # reset game
                return True
            elif user_input[0].lower() == 'q':
                return False
            else:
                print('Invalid input')


if __name__ == "__main__":
    HangmanGame().play()
