

class Matrix:
    """
    Constructed matrix is in a 'list of lists' form:
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
    """

    def __init__(self, mtrx=None):
        self.matrix = [[]] if mtrx is None else mtrx
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    def __str__(self):
        """:return: matrix row by row"""
        result = ''
        for i in range(self.rows):
            result += f'{" ".join([str(num) for num in self.matrix[i]])}\n'
        return result

    def add(self, mtrx2):
        """
        Add this matrix with another matrix (this + other).
        :return: a new Matrix object
        """
        if (self.rows, self.cols) != (mtrx2.rows, mtrx2.cols):
            print('The operation cannot be performed.')
            return None
        mtrx = [[self.matrix[r][c] + mtrx2.matrix[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return Matrix(mtrx)

    def subtract(self, mtrx2):
        """
        Subtract another matrix from this matrix (this - other).
        :return: a new Matrix object
        """
        if (self.rows, self.cols) != (mtrx2.rows, mtrx2.cols):
            print('The operation cannot be performed.')
            return None
        mtrx = [[self.matrix[r][c] - mtrx2.matrix[r][c] for c in range(self.cols)] for r in range(self.rows)]
        return Matrix(mtrx)

    def multiply(self, factor):
        """
        Multiply this matrix by another matrix (this * other).
        :param factor: Another matrix.
            If the parameter is a scalar, __multiply_by_scalar() is called instead.
        :return: a new Matrix object
        """
        if isinstance(factor, Matrix):
            mtrx2 = factor
            if self.cols != mtrx2.rows:
                print('The operation cannot be performed.')
                return None
            mtrx = [[sum([self.matrix[ra][rb] * mtrx2.matrix[rb][cb] for rb in range(mtrx2.rows)]) 
                    for cb in range(mtrx2.cols)] for ra in range(self.rows)]
            return Matrix(mtrx)
        else:
            return self.__multiply_by_scalar(factor)

    def __multiply_by_scalar(self, scalar):
        """
        Multiply this matrix by a scalar
        :return: a new Matrix object
        """
        mtrx = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(self.matrix[r][c] * scalar)
            mtrx.append(row)
        return Matrix(mtrx)

    def transpose(self, line='main'):
        """
        Transpose matrix by main diagonal by default. Other options available by specified line.
        :param line: transposition option ('main', 'side', 'horizontal', 'vertical') 
        :return: a new Matrix object
        """
        mtrx = None
        if line == 'main':
            mtrx = [[self.matrix[r][c] for r in range(self.rows)] for c in range(self.cols)]
        elif line == 'side':
            mtrx = [[self.matrix[r-1][c-1] for r in range(self.rows, 0, -1)] for c in range(self.cols, 0, -1)]
        elif (line == 'horizontal'):
            mtrx = [self.matrix[r-1] for r in range(self.rows, 0, -1)]
        elif (line == 'vertical'):
            mtrx = [[self.matrix[r][c-1] for c in range(self.cols, 0, -1)] for r in range(self.rows)]
        return Matrix(mtrx)

    def determinant(self):
        """
        Calculate the matrix determinant
        :return: a numeric value
        """
        if self.rows != self.cols:
            print('This is not a square matrix. Operation cannot be performed.')
            return None

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
            determinant += self.__cofactor(self.rows, self.cols)
            return determinant

    def inverse(self):
        """
        Calculate the inverse of a matrix.
        :return: a new Matrix object
        """
        try: 
            scalar = 1 / self.determinant()
        except ZeroDivisionError:
            print('Inversion for this matrix is not possible because its determinant equals 0')
            return None
        cofactors = self.__cofactor_matrix().transpose('main')
        mtrx = []
        for r in range(cofactors.rows):
            row = []
            for c in range(cofactors.cols):
                row.append(scalar * cofactors.matrix[r][c])
            mtrx.append(row)
        return Matrix(mtrx)

    def __cofactor_matrix(self):
        """
        Calculate the matrix of cofactors of this matrix
        :return: a new Matrix object
        """
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
                row.append(self.__cofactor(i,j))
            mtrx.append(row)
        return Matrix(mtrx)

    def __cofactor(self, i, j):
        """
        Helper of determinant() and __cofactor_matrix().
        calculates the cofactor of a matrix element based on its coordinates.
        :return: the cofactor of an element.
        """
        element_sign = (-1)**(i+j)
        minor_matrix = self.__minor_matrix(i, j)
        current_row, current_col, determinant = 0, 0, 0
        while current_col < minor_matrix.cols:
            mtrx_det = minor_matrix.__minor_matrix(current_row, current_col)
            sign = minor_matrix.__sign(current_row, current_col)
            determinant += sign * mtrx_det.determinant()  # recursion
            current_col += 1
        return element_sign * determinant
    
    def __sign(self, i, j):
        """
        Helper of cofactor().
        Finds the correct sign of the element to be multiplied with its determinant.
        formula: element * (-1) ** (row + column)
        :return: a signed element
        """
        return self.matrix[i][j] * (-1)**(i + j)

    def __minor_matrix(self, i, j):
        """
        Helper of __cofactor().
        Calculate the minor matrix based on the coordinates of an element.
        :return: a new Matrix object
        """
        mtrx = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                if (r != i) and (c != j):
                    row.append(self.matrix[r][c])
            if row:
                mtrx.append(row)
        return Matrix(mtrx)
