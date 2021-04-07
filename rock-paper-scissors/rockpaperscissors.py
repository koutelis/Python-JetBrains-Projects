import random


def display_logo():
    logo = """.--.         .      .--.                      .-.                               
|   )        |      |   )                    (   )      o                       
|--' .-.  .-.|.-.   |--'.-.  .,-.  .-. .--.   `-.  .-.  .  .--..--. .-. .--..--.
|  \(   )(   |-.'   |  (   ) |   )(.-' |     (   )(     |  `--.`--.(   )|   `--.
'   ``-'  `-''  `-  '   `-'`-|`-'  `--''      `-'  `-'-' `-`--'`--' `-' '   `--'
                             |                                                  
                             '"""
    print(logo)


class RockPaperScissors:

    scores_filepath = 'rating.txt'
    scores = {}
    points = {'win': 50, 'draw': 0, 'loss': -50}

    def __init__(self):
        display_logo()
        self.player = Player()
        RockPaperScissors.scores[str(self.player)] = 0
        self.moves = None
        self.active = True
    
    def __str__(self):
        return ''
    
    def __greet_player(self):
        print('\n' * 4 + f'Hello {self.player} !!!' + '\n' * 4)
    
    def __set_complexity(self):
        self.moves = self.__select_complexity()
    
    def __select_complexity(self):
        """:return: an odd-numbered list of moves based on user input"""
        print('Choose one of the following options:')
        print(' [3] Rock, Paper, Scissors   (default)')
        print(' [5] Rock, Paper, Scissors, Lizard, Spock')
        print(' [7] Rock, Paper, Scissors, Fire, Air, Water, Sponge')
        print('[15] Rock, Fire, Scissors, Snake, Human, Tree, Wolf, Sponge, Paper, Air, Water, Dragon, Devil, Lightning, Gun')
        print(' [#] Custom moves\n')

        while True:
            print('Choose number of moves: ')
            user_input = input('> ')
            if (len(user_input) == 0) or (user_input == '3'):
                return ['rock', 'paper', 'scissors']
            elif (user_input == '5'):
                return ['rock', 'paper', 'scissors', 'spock', 'lizard']
            elif (user_input == '7'):
                return ['rock', 'paper', 'fire', 'water', 'scissors', 'air', 'sponge'] 
            elif (user_input == '15'):
                return ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']
            elif (user_input == '#'):
                return self.__custom_complexity()
            else:
                print('Invalid input.')

    def __custom_complexity(self):
        """
        Helper of select_complexity().
        :return: an odd-numbered list of game moves.
        """
        while True:
            try:
                print('Write your own odd-numbered list of available moves separated by comma (,): ')
                user_list = input('> ').lower().split(',')
                user_list = [word.strip() for word in user_list]
                if not all(word.isalpha() for word in user_list):
                    print('Use only English alphabetical characters and no spaces')
                elif len(user_list) < 3:
                    print('Invalid input')
                elif len(user_list) % 2 == 0:
                    print('Your have to select an odd number of moves.')
                elif (len(user_list) % 2 != 0):
                    return user_list
                else:
                    print('Invalid input.')
            except:
                print('Invalid input.')
    
    @classmethod
    def read_scoring_history(cls):
        """
        Read saved scores from a file.
        Set the dictionary of scores based on the file.
        """
        open(cls.scores_filepath, 'a').close()
        with open(cls.scores_filepath, 'r') as f:
            for line in f.readlines():
                k, v = line.strip().split()
                cls.scores[k] = int(v)
    
    @classmethod
    def save_scores(cls):
        """saves the score dictionary to a file."""
        with open(cls.scores_filepath, 'w') as f:
            for player, score in cls.scores.items():
                print(f'{player} {score}', file=f)
    
    def __set_score(self, state):
        """updates player's score points."""
        scores = RockPaperScissors.scores
        points = RockPaperScissors.points
        player = str(self.player)
        scores[player] += points[state]
        if scores[player] < 0:
            scores[player] = 0
    
    def __display_score(self):
        """Display player's current score."""
        pts = RockPaperScissors.scores[str(self.player)]
        print(f'You have {pts} points.')
    
    def __menu(self):
        """Player inputs a move or a command."""
        print("Type one of the following options:\n")
        print(f" * Your move: {self.moves}")
        print(" * 'score' to see your rating")
        print(" * 'exit' to quit the game")
        user_input = input('> ').lower()
        print('\n' * 4)
        if user_input == 'exit':
            self.__exit()
        elif user_input == 'score':
            self.__display_score()
        elif user_input in self.moves:
            cpu_move = random.choice(self.moves)
            self.__compare_moves(user_input, cpu_move)
        else:
            print('Invalid input.')
    
    def __exit(self):
        """Performs actions need to be taken before closing."""
        self.active = False
        RockPaperScissors.save_scores()
        print('Thank you for playing!\n')
        display_logo()
    
    def __stronger_than(self, move):
        """
        :param move: a move
        :returns: a list of moves that defeat the given argument.
        """
        stronger = []
        for n in range(len(self.moves) // 2):
            i = (self.moves.index(move) + 1 + n * 2) % len(self.moves)
            stronger.append(self.moves[i])
        return stronger
    
    def __compare_moves(self, pl_move, cpu_move):
        """
        Compares the moves of player vs. cpu and display the result.
        Also updates the score accordingly.
        """
        if pl_move == cpu_move:
            self.__set_score('draw')
            print(f"Draw. You both chose '{cpu_move}'.")
        elif pl_move in self.__stronger_than(cpu_move):
            self.__set_score('win')
            print(f"You win! The computer chose '{cpu_move}' and your '{pl_move}' beats that.")
        else:
            self.__set_score('loss')
            print(f"Sorry, but the computer chose '{cpu_move}' which beats your '{pl_move}'.")

    def play(self):
        """Run this method to start the game."""
        self.__greet_player()
        self.__set_complexity()
        RockPaperScissors.read_scoring_history()
        print("Okay, let's start!" + "\n" * 10)
        while self.active:
            self.__menu()


class Player:

    def __init__(self):
        self.name = self.__input_name()
    
    def __str__(self):
        return self.name
    
    def __input_name(self):
        while True:
            name = input('Enter your name: ').lower()
            if (len(name) > 0) and name.isalpha():
                return name
            print('Invalid, please try again...')
