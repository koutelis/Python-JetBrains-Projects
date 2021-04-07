from random import choice


class Bot:
    """
    A simple conversational bot for Python beginners.
    Able to greet, ask user's name, guess their age, count and challenge knowledge .

    :param name: Bot's name
    :param year: Bot's year of creation
    :ivar name: See param name
    :ivar year: See param year
    """

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __greet(self):
        """Bot introduces itself"""
        print(f'Hello! My name is {self.name}.')
        print(f'I was created in {self.year} by HB.\n')

    @staticmethod
    def __ask_name():
        """Bot asks user's name, then responds."""
        print('Please, remind me your name.')
        name = input()
        print(f'What a great name you have, {name}!\n')

    @staticmethod
    def __guess_age():
        """Bot guesses user's age by asking a few math questions."""
        print('Let me guess your age.')
        rem3 = int(input('Divide your age by 3, what is the remainder? '))
        rem5 = int(input('Divide your age by 5, what is the remainder? '))
        rem7 = int(input('Divide your age by 7, what is the remainder? '))
        age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
        print(f"\nYour age is {age}; that's a good time to start programming!\n")

    @staticmethod
    def __count():
        """Bot asks user for a number and starts counting from 0 to that number."""
        print('Now I will prove to you that I can count to any number you want.\n')
        num = int(input('Enter max number: '))
        for i in range(num + 1):
            print(f'{i}!')
        print()

    @staticmethod
    def __ask_question():
        """Asks the user a question, then prints the answer."""
        # Programming questions and answers. Add more in the form of dictionary
        q_and_a = {'Why do we use methods?': 'To decompose a program into several small subroutines.',
                   'Who created Python?': 'Guido van Rossum'}
        print("\nLet's test your programming knowledge:\n")
        question = choice(list(q_and_a.keys()))
        answer = q_and_a[question]
        print(f'{question}')
        input('(Press a key to continue...)\n')
        print(answer)
    
    def chat(self):
        self.__greet()
        self.__ask_name()
        self.__guess_age()
        self.__count()
        self.__ask_question()

    @staticmethod
    def shutdown():
        print('\nHave a nice day!')


def run():
    """Use this function to start a chatty bot."""
    bot = Bot('Ash 2X3ZB9CY', 2013)
    bot.chat()
    bot.shutdown()
