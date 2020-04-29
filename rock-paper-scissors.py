from random import choice
from time import sleep

def logo():
    logo = """.--.         .      .--.                      .-.                               
|   )        |      |   )                    (   )      o                       
|--' .-.  .-.|.-.   |--'.-.  .,-.  .-. .--.   `-.  .-.  .  .--..--. .-. .--..--.
|  \(   )(   |-.'   |  (   ) |   )(.-' |     (   )(     |  `--.`--.(   )|   `--.
'   ``-'  `-''  `-  '   `-'`-|`-'  `--''      `-'  `-'-' `-`--'`--' `-' '   `--'
                             |                                                  
                             '"""
    return logo


def name():
    while True:
        name = input('Enter your name: ').lower()
        if (len(name) > 0) and name.isalpha():
            return name


def all_moves():
    """returns an odd list of moves based on user input"""
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
            ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']
        elif (user_input == '#'):
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
        else:
            print('Invalid input.')


def scoring(condition):
    """updates user score points"""
    scores[username] += points[condition]
    if scores[username] < 0:
        scores[username] = 0


def read_scoring(path):
    """returns a dictionary of scores saved in a file"""
    open(path, 'a').close()
    with open(path, 'r') as f:
        scores = {username: 0}
        for line in f.readlines():
            k, v = line.strip().split()
            scores[k] = int(v)
        return scores


def save_scoring(path):
    """saves the score dictionary to the file"""
    with open(path, 'w') as f:
        for user, score in scores.items():
            print(f'{user} {score}', file=f)


def gameplay():
    if human_mv == 'exit':
        print('Thank you for playing!\n')
        return False
    elif human_mv == 'score':
        print(f'You have {scores[username]} points.')
    elif human_mv in moves:
        if human_mv == cpu_mv:
            scoring('draw')
            print(f"Draw. You both chose '{cpu_mv}'.")
        elif human_mv in stronger_than(cpu_mv):
            scoring('win')
            print(f"You win! The computer chose '{cpu_mv}' and your '{human_mv}' beats that.")
        else:
            scoring('loss')
            print(f"Sorry, but the computer chose '{cpu_mv}' which beats your '{human_mv}'.")
    else:
        print('Invalid input.')

    sleep(0.2)
    return True


def stronger_than(move):
    """returns a list stronger moves compared to the move-argument"""
    stronger = []
    for n in range(len(moves) // 2):
        i = (moves.index(move) + 1 + n * 2) % len(moves)
        stronger.append(moves[i])
    return stronger


# init
print(logo())
username = name()
print('\n' * 4 + f'Hello {username} !!!' + '\n' * 4)
sleep(1)
moves = all_moves()
points = {'win': 50, 'draw': 0, 'loss': -50}

# read scoring history
scores = read_scoring('rating.txt')
print("Okay, let's start!" + "\n" * 10)

gaming = True
while gaming:
    print("Type one of the following options:\n")
    print(" * Your move: {}".format(moves))
    print(" * 'score' to see your rating")
    print(" * 'exit' to quit the game")
    human_mv = input('> ').lower()
    cpu_mv = choice(moves)
    print('\n' * 4)
    gaming = gameplay()    

# save scoring to file on !exit
save_scoring('rating.txt')
print(logo())
