import predictor


class Game:
    """
    The player starts with a virtual capital.
    Every time the computer guesses a symbol correctly, the player loses one dollar.
    Every time the system is wrong, the player gains one dollar.
    
    :ivar predictor: Class responsible for predicting binary digits
    :ivar capital: Integer. The amount of virtual dollars the player starts with.
    """

    def __init__(self, capital):
        self.predictor = predictor.Predictor()
        self.capital = capital
        print(f'You have ${capital}. Every time the system successfully predicts your next press, you lose $1.')
        print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')

    def play(self):
        """
        Initiates a game of predictions.
        Repeats multiple rounds until user either quits or loses all capital.
        """
        active = True
        while active:
            active = self.__play_round()
        print('Game over!')

    def __play_round(self):
        """Helper of play(). Single game round."""
        test_data = self.predictor.more_data()
        if test_data is None:
            return False
        else:
            self.predictor.analyze_data(test_data)
            prediction = self.predictor.predict(test_data)
            self.__round_result(test_data, prediction)
        return self.capital > 0

    def __round_result(self, test_data, prediction):
        """
        Compares two strings of equal length.
        Prints the percentage of the correctly predicted characters excluding the first 3.
        Updates capital based on cpu success.
        :param test_data: a string of 1s and 0s
        :param prediction: a string of 1s and 0s
        """
        assert len(test_data) == len(prediction)
        total = len(test_data) - 3
        total_guessed = 0
        for i in range(3, len(test_data)):
            if test_data[i] == prediction[i]:
                total_guessed += 1
        percentage = total_guessed / total * 100
        print('Computer guessed right {} out of {} symbols ({:03.2f} %)'.format(total_guessed, total, percentage))
        amount = total - (2 * total_guessed)
        self.capital += amount
        print(f'Your capital is now ${self.capital}')
