import hangman_ascii as hascii


class Hangman:
    """
    Simple terminal-based hangman game.
    """

    def __init__(self, word):
        self.word = word
        self.letters = list(word)
        self.letters_hid = list('-' * len(word))
        self.prev_guesses = ''
        self.lives = self.choose_difficulty()

    def __str__(self):
        word_hid = ''.join(self.letters_hid)
        output = f'{hascii.figure[self.lives]}\nword: {word_hid}'
        return output

    @staticmethod
    def choose_difficulty():
        """Select difficulty (number of lives) for the hangman game."""
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
            except ValueError:
                print('Invalid input')

    def guess(self, letter):
        """Display the result after a guess and update accordingly."""
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
    
    def is_saved(self):
        """:return: True if hangman is saved, else false"""
        word_hid = ''.join(self.letters_hid)
        return word_hid == self.word
    
    def is_hanged(self):
        """:return: True if hangman is hanged, else false"""
        return self.lives == 1
