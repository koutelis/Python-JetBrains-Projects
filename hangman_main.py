# Write your code here
import random
import string
import hangman_ascii as hascii

class Hangman:

    lives = 9

    def __init__(self, word):
        self.word = word
        self.letters = list(word)
        self.letters_hid = list('-' * len(word))
        self.prev_guesses = ''

    def __str__(self):
        self.word_hid = ''
        for char in self.letters_hid:
            self.word_hid += char
        return self.word_hid

    def letter_guess(self, letter):

        if letter in self.prev_guesses:
            print('\nYou already typed this letter')
        elif letter not in self.word:
            self.prev_guesses += letter
            self.lives -= 1
            print('\nNo such letter in the word')
        else:
            self.prev_guesses += letter 

        for i in range(len(self.letters)):
            if letter == self.letters[i]:
                self.letters_hid[i] = letter   

        return self.__str__()

def difficulty():
    print('Difficulty levels:')
    print('-----------------')
    print('1: easy - 12 lives)')
    print('2: medium - 9 lives)')
    print('3: hard - 6 lives)\n')
    diff = {1: 12, 2: 9, 3: 6}

    while True:
        try:
            level = int(input('Select 1 2 or 3: '))
            if level in diff.keys():
                return diff[level]
            else:
                print('Invalid input')
        except:
            print('Invalid input')

def replay():
    while True:
        try:
            user_input = input('\nWould you like to [R]eplay or [Q]uit?: ')
            if user_input[0].lower() == 'r':
                return 1
            elif user_input[0].lower() == 'q':
                return 0
            else:
                print('Invalid input')
        except:
            print('Invalid input')


def is_valid_letter(letter):
    """checks if character is single English lowercase letter"""
    if len(letter) != 1:
        print('You should input a single letter')
        return False
    if letter not in string.ascii_letters:
        print('You did not input a valid English letter')
        return False
    return True

def hang_stage():
    return hascii.stage12


if __name__ == "__main__":

    # init
    with open('hangman_words.txt', 'r') as text:
        """all words are lowercase"""
        wordlist = [word.rstrip() for word in text]

    active = True

    # main
    while active:
        print(hascii.logo)
        print()
        Hangman.lives = difficulty()
        hangman = Hangman(random.choice(wordlist))

        while True:
            print(hascii.figure[hangman.lives])
            print()
            print(f'word: {hangman}')
            print(f'\nNumber of lives left: {hangman.lives}\n')

            # user plays
            guess = input('Input a letter: ').lower()
            if is_valid_letter(guess):
                hangman.letter_guess(guess)
                # check winning condition
                if hangman.word_hid == hangman.word:
                    print(hascii.figure['free'])
                    print('\nYou survived!')
                    break
                        
                # check lives
                if hangman.lives == 1:
                    print(hascii.figure[1])
                    print('\nYou are hanged!')
                    print(f'The word was {hangman.word}')
                    break
                
            print()

        active = replay()

    print('\nThank you for playing!')
    print(hascii.logo)
