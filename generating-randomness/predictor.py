import random


class Predictor:
    """
    This class takes data in the form of string consisting binary digits.
    These digits can form 8 permutations of triads consisting of 1s and 0s:
    {000, 001, 010, 011, 100, 101, 110, 111}.
    This class gathers statistics about the digit following each of the 8 groups,
    how many times a group is followed by 0 and how many times followed by 1.

    The statistics are stored in a dictionary,  in the format k: [a, b]
    where k is the triad string and the value is a list of two integers,
    a = counts of 0 (how many times the triad is followed by a '0')
    b = counts of 1 (how many times the triad is followed by a '1')

    :cvar binary: a list of the only two allowed binary values (strings)
    :ivar stats: a dictionary to store statistics about binary digits
    """

    binary = ['0', '1']

    def __init__(self):
        self.stats = {k: [0, 0] for k in [format(n, 'b').zfill(3) for n in range(2 ** 3)]}
        self.analyze_data(self.initial_data(100))

    def analyze_data(self, data):
        """
        This function scans the data for each triadic permutation updates self.stats.
        See class definition for more info.
        :param data: a string to be analyzed.
        """
        for i in range(len(data) - 3):
            triad = data[i:i + 3]
            next_symbol = data[i + 3]
            if next_symbol == '0':
                self.stats[triad][0] += 1
            else:  # next_symbol == '1'
                self.stats[triad][1] += 1

    def initial_data(self, min_length):
        """
        Request data from the user, repeatedly until min_length is met or exceeded.
        :param min_length: the minimum length of the string to be returned.
        :return: A string of more than or equal to specified length, consisting of 1s and 0s.
        """
        print('Please give AI some data to learn...')
        data = ''
        while len(data) < min_length:
            remaining = min_length - len(data)
            print(f'The current data length is {len(data)}, {remaining} symbols left')
            print('Print a random string containing 0 or 1:\n')
            data += self.__filter_data(input())
        print('\nFinal data string:')
        print(data + '\n')
        return data

    def more_data(self):
        """
        Request data from the user, repeatedly if filtered input length is less than 4.
        :return: A string consisting of 1s and 0s.
        """
        print('\nPrint a random string containing 0 or 1:')
        test_data = input()
        if test_data == 'enough':
            return None
        test_data = self.__filter_data(test_data)
        return test_data if len(test_data) > 3 else self.more_data()

    @classmethod
    def __filter_data(cls, data):
        """
        Helper of initial_data() and more_data().
        Filters out irrelevant symbols (anything other than '1' and '0') from given data.
        :param data: a string to be filtered.
        :return: Filtered string of 1s and 0s.
        """
        filtered = ''
        for digit in data:
            if digit in cls.binary:
                filtered += digit
        return filtered

    def predict(self, test_data):
        """
        The first 3 binary digits are random.
        The rest are based on statistical analysis from given stats.
        Prints and returns prediction.
        :param test_data: the target string to be predicted.
        :return: a predicted string of 1s and 0s.
        """
        prediction = []
        for _ in range(3):
            prediction.append(random.choice(Predictor.binary))
        while len(prediction) < len(test_data):
            current_triad = test_data[len(prediction)-3:len(prediction)]
            if self.stats[current_triad][1] > self.stats[current_triad][0]:
                next_digit = '1'
            elif self.stats[current_triad][1] < self.stats[current_triad][0]:
                next_digit = '0'
            else:
                next_digit = random.choice(['0', '1'])
            prediction.append(next_digit)
        guessed_data = ''.join(prediction)
        print(f'prediction:\n{guessed_data}\n')
        return guessed_data
