import games
from random import choice
import input_handler as handler 

class Robogotchi:

    def __init__(self):
        self.name = handler.robogotchi_name_input()
        self.active = False
        self.stats = {'battery': 100, 'battery_prev': 100, 'overheat': 0, 'overheat_prev': 0,
                      'skill': 0, 'skill_prev': 0, 'boredom': 0, 'boredom_prev': 0,
                      'rust': 0, 'rust_prev': 0}

    def __str__(self):
        return self.name

    def run(self):
        """Run this method to activate Robogotchi."""
        self.__activate()
        while self.active:
            self.__menu()
            if not self.active:
                self.__repair()

    def __take_action(self, action):
        """
        Interract with Robogotchi with these actions.
        """
        if action == 'exit':
            self.__deactivate('Game over')
        elif action == 'info':
            self.__info()
        elif action == 'work':
            self.__work()
        elif action == 'play':
            self.__play()
        elif action == 'oil':
            self.__oil()
        elif action == 'recharge':
            self.__recharge()
        elif action == 'sleep':
            self.__sleep()
        elif action == 'learn':
            self.__learn()

    def __info(self):
        """
        Display Robogotchi's stats (vitals).
        """
        print(f'{self}\'s stats are:')
        print(f'\t* battery is {self.stats["battery"]},')
        print(f'\t* overheat is {self.stats["overheat"]},')
        print(f'\t* skill level is {self.stats["skill"]},')
        print(f'\t* boredom is {self.stats["boredom"]},')
        print(f'\t* rust is {self.stats["rust"]}.\n')

    def __work(self):
        """
        One of Robogotchi's actions. Does chores where mishaps may happen.
        """
        if self.stats['skill'] < 50:
            print(f'{self} has got to learn before working!\n')
        else:
            self.__change_stat('battery', -10)
            self.__change_stat('boredom', +10)
            self.__change_stat('overheat', +10)
            self.__random_mishap()
            self.__display_stat('boredom', 'overheat', 'battery', 'rust')
            print(f'\n{self} did well!\n')

    def __play(self):
        """
        One of Robogotchi's actions. Plays a game where mishaps may happen.
        """
        game = games.select_game()
        if game:
            game.play()
            self.__change_stat('boredom', -10)
            self.__change_stat('overheat', +10)
            game.display_stats()
            self.__random_mishap()
            if not self.active:
                return
            self.__display_stat('boredom', 'overheat', 'rust')

        if self.stats['boredom'] == 0:
            print(f'\n{self} is in a great mood!')
        print()

    def __oil(self):
        """
        One of Robogotchi's actions. Oil the robot to remove some amount of rust.
        """
        if self.stats['rust'] == 0:
            print(f'{self} is fine, no need to oil!\n')
        else:
            self.__change_stat('rust', -20)
            self.__display_stat('rust')
            print(f'\n{self} is less rusty!\n')

    def __recharge(self):
        """
        One of Robogotchi's actions. Recharge some amount of battery.
        """
        if self.stats['battery'] == 100:
            print(f'{self} is charged!\n')
        else:
            self.__change_stat('overheat', -5)
            self.__change_stat('battery', +10)
            self.__change_stat('boredom', +5)
            self.__display_stat('overheat', 'battery', 'boredom')
            print()
            print(f'{self} is recharged!\n')

    def __sleep(self):
        """
        One of Robogotchi's actions. Enters sleep mode.
        """
        if self.stats['overheat'] == 0:
            print(f'{self} is cool!\n')
        else:
            self.__change_stat('overheat', -20)
            self.__display_stat('overheat')
            print()
            if self.stats['overheat'] == 0:
                print(f'{self} is cool!\n')
            else:
                print(f'{self} cooled off!\n')

    def __learn(self):
        """
        One of Robogotchi's actions. Learns a new skill and becomes smarter.
        """
        if self.stats['skill'] == 100:
            print(f'There\'s nothing for {self} to learn!\n')
        else:
            self.__change_stat('skill', +10)
            self.__change_stat('overheat', +10)
            self.__change_stat('battery', -10)
            self.__change_stat('boredom', +5)
            self.__display_stat('skill', 'overheat', 'battery', 'boredom')
            print(f'\n{self} has become smarter!\n')

    def __random_mishap(self):
        """
        There is a 75% change that Robogotchi might get wet during working or playing,
        where as a consequence will become rusty.
        """
        mishaps = {'none': 0, 'puddle': 10, 'sprinkler': 30, 'pool': 50}
        mishap = choice(list(mishaps.keys()))
        if mishap == 'puddle':
            msg = f'Oh no, {self} stepped into a puddle!'
        elif mishap == 'sprinkler':
            msg = f'Oh, {self} encountered a sprinkler!'
        elif mishap == 'pool':
            msg = f'Guess what! {self} fell into the pool!'
        else:
            return
        print(msg + "\n")
        self.__change_stat('rust', mishaps[mishap])

    def __change_stat(self, stat, diff):
        """
        Change one of Robogotchi's stats. A consequence of most of its actions.
        :param stat: the stat to be changed
        :param diff: the amount to increment/decrement a stat
        """
        self.stats[f'{stat}_prev'] = self.stats[stat]
        self.stats[stat] = self.__equalize_value(self.stats[stat] + diff)
        stat_value = self.stats[stat]
        if stat == 'rust' and stat_value == 100:
            self.__deactivate(f'{self} is too rusty! Repair it.')
        elif stat == 'overheat' and stat_value == 100:
            self.__deactivate(f'The level of overheat reached 100, {self} has blown up! Game over.')
        elif stat == 'boredom' and stat_value == 100:
            self.__deactivate('f{self} is too bored! Do something.')
        elif stat == 'battery' and stat_value == 0:
            self.__deactivate('f{self} Battery drained! Do something.')

    def __activate(self):
        """Activate Robogotchi"""
        self.active = True

    def __deactivate(self, reason):
        """
        Deactivate Robogotchi
        :param reason: a reason for deactivation, either game over or a major malfunction.
        """
        self.active = False
        print(reason)
        if self.stats['overheat'] == 100:
            raise SystemExit

    def __display_stat(self, *args):
        """
        Displays the level of the given stat(s).
        """
        for stat in args:
            previous = self.stats[f'{stat}_prev']
            current = self.stats[stat]
            if stat == 'battery':
                print(f'{self}\'s level of the {stat} was {previous}. Now it is {current}.')
            else:
                print(f'{self}\'s level of {stat} was {previous}. Now it is {current}.')

    def __menu(self):
        """Robogotchi's main menu. Input is handled elsewhere."""
        option_list = ['exit', 'info', 'work', 'play', 'oil', 'recharge', 'sleep', 'learn']
        action = handler.robogotchi_menu_input(self, option_list)
        self.__take_action(action)

    def __broken_menu(self, problem_desc, mandatory_option):
        """
        Helper of __repair()
        Robogotchi's broken menu. Input is handled elsewhere.
        """
        broken_option_list = ['exit', 'oil', mandatory_option]
        while True:
            print(problem_desc)
            action = handler.robogotchi_menu_input(self, broken_option_list, broken=True)
            self.__take_action(action)
            if action == mandatory_option:
                self.__activate()
                return

    def __repair(self):
        """
        The robot enters this state, when it reaches certain limits and cannot perform certain actions.
        A different menu will be working instead.
        """
        if self.stats['overheat'] == 100:
            return  # forever broken
        if self.stats['battery'] == 0:
            problem_desc = f'The level of the battery is 0, {self} needs recharging!\n'
            self.__broken_menu(problem_desc, 'recharge')
        elif self.stats['boredom'] == 100:
            problem_desc = f'{self} is too bored! {self} needs to have fun!\n'
            self.__broken_menu(problem_desc, 'play')

    @staticmethod
    def __equalize_value(value):
        """
        Helper of __change_stat(). Limiter of value to stay within 0-100 inclusive.
        :return: an integer value 0-100
        """
        if value > 100:
            return 100
        elif value < 0:
            return 0
        return value
    
