import games


class InvalidInputException(ValueError):
    pass


def robogotchi_name_input():
    """
    Request input from the user, concerning the robogotchi's name.
    :return: a name
    """
    robot_name = input('How will you call your robot?\n')
    print()
    return robot_name


def robogotchi_menu_input(robo, option_list, broken=False):
    """
    Request input from the user, concerning the robogotchi main menu.
    :return: an action from the option_list
    """
    normal_option_list = ['exit', 'info', 'work', 'play', 'oil', 'recharge', 'sleep', 'learn']
    normal_indexes = [str(i) for i in range(len(normal_option_list))]
    option_dict = {'exit': '\n\t0. Exit', 'info': '\n\t1. Check the vitals', 'work': '\n\t2. Work',
                'play': '\n\t3. Play', 'oil': '\n\t4. Oil', 'recharge': '\n\t5. Recharge',
                'sleep': '\n\t6. Sleep mode', 'learn': '\n\t7. Learn skills'}
    options = f'Available interactions with Robogotchi {robo}:'
    options += ''.join(option_dict[option] for option in option_list) + '\n'
    while True:
        print(options)
        user_input = input('Choose:\n')
        print()
        
        if user_input not in normal_indexes:
            print('Invalid input, try again!\n')
        else:
            if not broken:
                return normal_option_list[int(user_input)]
            else:
                broken_option_list = [x if x in option_list else None for x in normal_option_list]
                broken_indexes = [str(i) for i, opt in enumerate(broken_option_list) if opt is not None]
                if user_input in broken_indexes:
                    return broken_option_list[int(user_input)]
                elif user_input in normal_indexes:
                    print('{self} cannot perform this action right now...')
                else:
                    print('Invalid input, try again!\n')


def game_input(game):
    """
    Request input from the user, concerning the robogotchi mini-games.
    """
    while True:
        if isinstance(game, games.NumberGame):
            question = "Select a number 1 - 1000000, or type 'exit'.\n"
        elif isinstance(game, games.RockPaperScissors):
            question = "Select a move (rock paper scissors), or type 'exit'\n"
        else:
            raise TypeError('Invalid game\n')

        user_input = input(question)
        print()
        if user_input == 'exit':
            return user_input
        else:
            try:
                return __validate_game_input(game, user_input)
            except InvalidInputException as e:
                print('Invalid input\n')


def __validate_game_input(game, inpt):
    """
    Helper of take_input(). Validate user input
    :return: user's input if valid, else raise InvalidInputException
    """
    if isinstance(game, games.NumberGame):
        try:
            inpt = int(inpt)
        except ValueError:
            raise InvalidInputException('A string is not a valid input!\n')
        if inpt > 1_000_000:
            raise InvalidInputException('Invalid input! The number can\'t be bigger than 1000000\n')
        elif inpt < 0:
            raise InvalidInputException('The number can\'t be negative!\n')
    elif isinstance(game, games.RockPaperScissors) and inpt not in game.options:
        raise InvalidInputException('No such option! Try again!\n')

    return inpt


def select_game():
    """
    User select a mini-game to play with Robogotchi.
    :return: a number (1 or 2), or None to exit.
    """
    print('Which game would you like to play?\n')
    print('\t1. numbers')
    print('\t2. rock-paper-scissors')
    user_input = input().lower()
    print()
    while True:
        if user_input == 'exit game':
            return None
        elif user_input == '1':
            return 1
        elif user_input == '2':
            return 2
        else:
            user_input = input("Please choose a valid option: '1' or '2'\n")
            print()
