from matrix import Matrix


class MatrixCalculator:

    def __create_matrix(self, name=''):
        """
        Create matrix based on user input.
        :return: a matrix in a list of lists form
        """
        print('To create a matrix, first input its size (rows x columns) with two numbers separated by space.')
        print('Then enter the matrix row by row with numbers separated by space.')
        while True:
            try:
                n, m = map(int, input(f'Enter size of {name}matrix: ').split())  # rows, cols
                print(f'Enter {name}matrix:')
                mtrx = self.__input_elements(n, m)
                return Matrix(mtrx)
            except ValueError:
                print('Invalid size input')

    @staticmethod
    def __input_elements(rows, cols):
        """
        Helper of __create_matrix().
        Takes user input row by row. 
        Input must be numeric and numbers must be separated by spaces for each row.
        :return: a list of lists consisting of float values"""
        while True:
            try:
                valid = True
                mtrx = []
                for row in range(rows):
                    row = [num for num in map(float, input().split())]
                    if len(row) == cols:
                        mtrx.append(row)
                    else:
                        print('Invalid input')
                        valid = False
                        break
            except ValueError:
                print('Invalid input')
                valid = False
            if valid:
                return mtrx
    
    @staticmethod
    def __input_scalar():
        while True:
            try:
                scalar = float(input('Enter constant: '))
                return scalar
            except ValueError:
                print('Invalid input')

    @staticmethod
    def __transposition_type():
        """
        User chooses a type for matrix transposition.
        :return: a transposition option (string)
        """
        options = {'1': 'main', '2': 'side', '3': 'vertical', '4': 'horizontal'}
        print('Transposition options:')
        print('\t1. Main diagonal')
        print('\t2. Side diagonal')
        print('\t3. Vertical line')
        print('\t4. Horizontal line')
        user_input = input('Your choice: ')
        return options[user_input]

    @staticmethod
    def __menu():
        """program options for the user"""
        print('Calculation options:')
        print('\t1. Add matrices')
        print('\t2. Subtract matrices')
        print('\t3. Multiply matrix by a constant')
        print('\t4. Multiply matrices')
        print('\t5. Transpose matrix')
        print('\t6. Calculate a determinant')
        print('\t7. Inverse matrix')
        print('\t0. Exit')
        user_input = input('Your choice: ')
        return user_input

    def run(self):
        """Run this function to start the matrix calculator."""
        while True:
            user_input = self.__menu()
            if user_input not in [str(i) for i in range(8)]:
                print('Invalid input')
                continue
            if user_input == '0':
                break
            if user_input in ['1', '2', '4']:
                matrix_a, matrix_b = self.__create_matrix('first '), self.__create_matrix('second ')
                if user_input == '1':
                    result = matrix_a.add(matrix_b)
                elif user_input == '2':
                    result = matrix_a.subtract(matrix_b)
                else:  # user_input == '4':
                    result = matrix_a.multiply(matrix_b)
            elif user_input in ['3', '5', '6', '7']:
                matrix = self.__create_matrix()
                if user_input == '3':
                    scalar = self.__input_scalar()
                    result = matrix.multiply(scalar)
                elif user_input == '5':
                    trnsp_type = self.__transposition_type()
                    result = matrix.transpose(trnsp_type)
                elif user_input == '6':
                    result = matrix.determinant()
                else:  # user_input == '7':
                    result = matrix.inverse()

            if result is not None:
                print('The result is:')
                print(result)
