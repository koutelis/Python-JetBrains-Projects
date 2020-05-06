### MATRIX CALCULATIONS ###

class Matrix:
    """constructed matrix is in a 'list of lists' form:
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
    """

    def __init__(self, mtrx=[[]]):
        self.rows = len(mtrx)
        self.cols = len(mtrx[0])
        self.matrix = mtrx


    def __str__(self):
        """prints matrix row by row"""
        result = ''
        for i in range(self.rows):
            result += f'{" ".join([str(num) for num in self.matrix[i]])}\n'
        return result


    def input_elements(self, rows, cols):
        """takes user inpup matrix, row by row and returns it as list with elements converted from str to float"""
        self.rows = rows
        self.cols = cols
        while True:
            try:
                constr = True
                mtrx = []
                for row in range(rows):
                    row = [num for num in map(float, input().split())]
                    if len(row) == self.cols:
                        mtrx.append(row)
                    else:
                        print('Invalid input')
                        constr = False
                        break
            except ValueError:
                print('Invalid input')
                constr = False
            if constr:
                self.matrix = mtrx
                break


    def addition(self, mtrx2):
        """adds this matrix to another matrix. Returns the resulting new matrix object"""
        if (self.rows, self.cols) != (mtrx2.rows, mtrx2.cols):
            print('The operation cannot be performed.')
            return False
        mtrx = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(self.matrix[r][c] + mtrx2.matrix[r][c])
            mtrx.append(row)
        return Matrix(mtrx)


    def multiplication_by_scalar(self):
        """multiplies this matrix by a scalar. Returns the resulting matrix"""
        try:
            scalar = float(input('Enter constant: '))
        except ValueError:
            print('Invalid input')
            return False
        else:
            mtrx = []
            for r in range(self.rows):
                row = []
                for c in range(self.cols):
                    row.append(self.matrix[r][c] * scalar)
                mtrx.append(row)
            return Matrix(mtrx)


    def multiplication(self, mtrx2):
        """multiplies this matrix (A) by another matrix (B). Returns the resulting AB matrix"""
        if self.cols != mtrx2.rows:
            print('The operation cannot be performed.')
            return False
        mtrx = []
        for ra in range(self.rows):
            row = []
            for cb in range(mtrx2.cols):
                sum = 0
                for rb in range(mtrx2.rows):
                    sum += self.matrix[ra][rb] * mtrx2.matrix[rb][cb]
                row.append(sum)
            mtrx.append(row)
        return Matrix(mtrx)


    def transposition(self, line='main'):
        """transposes matrix by main diagonal. Returns the resulting new matrix object"""
        mtrx = []
        if line == 'main':
            for c in range(self.cols):
                row = []
                for r in range(self.rows):
                    row.append(self.matrix[r][c])
                mtrx.append(row)
        elif line == 'side':
            for c in range(self.cols, 0, -1):
                row = []
                for r in range(self.rows, 0, -1):
                    row.append(self.matrix[r-1][c-1])
                mtrx.append(row)
        elif (line == 'horizontal') and (self.cols % 2 == 0):
            for r in range(self.rows, 0, -1):
                mtrx.append(self.matrix[r-1])
        elif (line == 'vertical') and (self.rows % 2 == 0):
            for r in range(self.rows):
                row = []
                for c in range(self.cols, 0, -1):
                    row.append(self.matrix[r][c-1])
                mtrx.append(row)
        else:
            print(f'Invalid size for {line} transposition')
            return False
        return Matrix(mtrx)


    def determinant(self):
        """calculates and returns the matrix determinant"""
        if self.rows != self.cols:
            print('This is not a square matrix. Operation cannot be performed.')
            return False

        # for matrix 1x1
        if self.rows == 1:
            return self.matrix[0][0]

        # for matrix 2x2
        if self.rows == 2:
            # get product of main diagonal
            main_diag = 1
            for r in range(self.rows):
                main_diag *= self.matrix[r][r]

            # get product of side diagonal
            r, c, side_diag = 0, (self.cols - 1), 1
            while (r < self.rows) and (c >= 0):
                side_diag *= self.matrix[r][c]
                r += 1
                c -= 1
            determinant = main_diag - side_diag
            return determinant

        # recursion if matrix bigger than 2x2
        else:
            determinant = 0
            determinant += self.cofactor(self.rows, self.cols)
            return determinant


    def sign(self, i, j):
        """returns the signed element to be multiplied with its determinant:
        element * (-1) to the power of row + column"""
        return self.matrix[i][j] * (-1)**(i + j)


    def cofactor(self, i, j):
        """calculates and returns the cofactor of a matrix element based on coordinates"""
        element_sign = (-1)**(i+j)
        minor_matrix = self.minor_matrix(i, j)
        current_row = 0
        current_col = 0
        determinant = 0
        while current_col < minor_matrix.cols:
            mtrx_det = minor_matrix.minor_matrix(current_row, current_col)
            sign = minor_matrix.sign(current_row, current_col)
            determinant += sign * mtrx_det.determinant()  # recursion
            current_col += 1
        return element_sign * determinant


    def minor_matrix(self, i, j):
        """returns the minor matrix of a matrix element based on its coordinates"""
        mtrx = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                if (r != i) and (c != j):
                    row.append(self.matrix[r][c])
            if row:
                mtrx.append(row)
        return Matrix(mtrx)


    def cofactor_matrix(self):
        """Returns the matrix of cofactors"""
        # for matrix 1x1
        if self.rows == 1:
            return self.matrix[0][0]

        # for matrix 2x2
        if self.rows == 2:
            a, b, c, d = self.matrix[0][0], self.matrix[0][1], self.matrix[1][0], self.matrix[1][1]
            return Matrix([[d, -c],[-b, a]])

        # matrices larger than 2x2    
        mtrx = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.cofactor(i,j))
            mtrx.append(row)
        return Matrix(mtrx)


    def inverse(self):
        """returns the inverse of a matrix, as a new matrix"""
        try: 
            scalar = 1 / self.determinant()
        except ZeroDivisionError:
            print('Inversion for this matrix is not possible because its determinant equals 0')
            return False
        cofactors = self.cofactor_matrix().transposition('main')
        mtrx = []
        for r in range(cofactors.rows):
            row = []
            for c in range(cofactors.cols):
                row.append(scalar * cofactors.matrix[r][c])
            mtrx.append(row)
        return Matrix(mtrx)


def transposition_type():
    """returns option for matrix transposition type"""
    while True:
        options = {'1': 'main', '2': 'side', '3': 'vertical', '4': 'horizontal'}
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        user_input = input('Your choice: ')
        return options[user_input]


def options():
    """program options for the user"""
    print('[[M, A, T],')
    print(' [R, +, I],')
    print(' [S, E, S]]')
    print('\n' * 4)
    while True:
        print('1. Add matrices')
        print('2. Multiply matrix by a constant')
        print('3. Multiply matrices')
        print('4. Transpose matrix')
        print('5. Calculate a determinant')
        print('6. Inverse matrix')
        print('0. Exit')
        user_input = input('Your choice: ')
        return user_input


def create_matrix(name=''):
    """Create a matrix based on user input. Returns matrix in a list of lists form"""
    print('To create a matrix, first input its size (rows x columns) with two numbers separated by space.')
    print('Then enter the matrix row by row with numbers separated by space.')
    while True:
        try:
            n, m = map(int, input(f'Enter size of {name}matrix: ').split())  # rows, cols
            mtrx = Matrix()
            print(f'Enter {name}matrix:')
            mtrx.input_elements(n, m)
            return mtrx
        except ValueError:
            print('Invalid size input')


def user_interaction():
    while True:
        UI = options()
        if UI == '0':
            break
        elif UI == '1':
            matrix_A = create_matrix('first ')
            matrix_B = create_matrix('second ')
            result = matrix_A.addition(matrix_B)
        elif UI == '2':
            matrix_A = create_matrix()
            result = matrix_A.multiplication_by_scalar()
        elif UI == '3':
            matrix_A = create_matrix('first ')
            matrix_B = create_matrix('second ')
            result = matrix_A.multiplication(matrix_B)
        elif UI == '4':
            trans_type = transposition_type()
            matrix_A = create_matrix()
            result = matrix_A.transposition(trans_type)
        elif UI == '5':
            matrix_A = create_matrix()
            result = matrix_A.determinant()
        elif UI == '6':
            matrix_A = create_matrix()
            result = matrix_A.inverse()
        else:
            print('Invalid input')

        if result:
            print('The result is:')
            print(result)


# MAIN
user_interaction()
