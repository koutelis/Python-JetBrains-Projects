from collections import deque

"""
Simple terminal-based calculator.
Supports addition, subtraction, multiplication, division, exponents and parentheses.

There is a small bug with negative integer parsing.
"""

# globals
variables = {}
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

def guide():
    """Display available commands to the user"""
    print('\nType:')
    print('====')
    print('/help')
    print('/exit')
    print('a mathematical expression\n')


def help():
    """Display available operations to the user."""
    print('Operations supported:')
    print('+ addition')
    print('- subtraction')
    print('* multiplication')
    print('/ division')
    print('^ exponent')
    print('() parentheses')
    print('for example: 3 * (4 + 5)^3 / 8 - 5')
    print('\nVariables can be stored in the form of: var = num')
    print('for example: x = 2, y = 4, ABC = 35\n')


def _command(command):
    """
    A command must start with a slash (/).
    :param command: A command that starts with a slash (e.g. /help)
    :return: False if user uses the exit command and True for any other input.
    """
    if command == '/exit':
        print('\nThank you for literally counting on us!')
        return False
    elif command == '/help':
        help()
    else:
        print('Unknown command')
    return True


def var_assign(x):
    """
    Populates the variables dictionary.
    :param x: an assignment expression in the format var = num
    """
    x = [item.strip() for item in x.split('=')]  # split expression terms
    term1, term2 = x[0], x[1]
    # check 1st term for valid identifier (no numbers or other characters)
    if term1.isalpha():
        # assignment must have two terms only
        if len(x) != 2:
            print('Invalid assignment')
        else:
            # if num, add to dict
            if term2.isnumeric():
                variables[term1] = int(term2)
            # check if 2nd term is already stored in dict, then add its value
            elif variables.get(term2):
                variables[term1] = variables[term2]
            elif not term2.isalpha():
                print('Invalid assignment')
            else:
                print('Unknown variable')
    else:
        print('Invalid identifier')


def validate_brackets(expression):
    """
    Validates the brackets of a mathematical expression for appropriate opening-closing.
    :param expression: a mathematical expression
    :return: True for valid brackets, else False
    """
    stack = deque()

    for item in expression:
        if item == '(':
            stack.append(item)
        elif item == ')':
            try:
                stack.pop()
            except IndexError:
                return False

    if not stack:
        return True
    return False


def infix_list(expression):
    """
    Convert a conventional mathematical expression to infix notation.
    :param expression: a mathematical expression.
    :return: a deque list of infix notation.
    """
    stack = deque()
    postfix = deque()
    if expression[:2] in '+ - * / ' or expression[0] in '*)':  # can't start with operator
        return None
    for char in expression:
        if stack:
            # checks for number operands
            if char.isnumeric():
                if stack[-1].isnumeric():
                    stack[-1] += char
                elif stack[-1].isalpha():
                    return None
                else:
                    stack.append(char)
            # checks for var operands
            elif char.isalpha():
                if stack[-1].isalpha():
                    stack[-1] += char
                elif stack[-1].isnumeric():
                    return None
                else:
                    stack.append(char)
            elif char == ' ' and stack[-1] != ' ':
                stack.append(char)
            elif char == '(':
                if stack[-1].isalnum():
                    return None
                stack.append(char)
            elif char == ')':
                if stack[-1] in '(-+*/':
                    return None
                stack.append(char)
            elif char == '-':
                if stack[-1] == '-':
                    stack.pop()
                    stack.append('+')
                elif stack[-1] == '+':
                    stack.pop()
                    stack.append(char)
                else:
                    stack.append(char)
            elif char == '+':
                if stack[-1] == '+':
                    continue
                else:
                    stack.append(char)
            elif char in '*/':
                if stack[-1] in '*/(':
                    return None
                stack.append(char)
        else:
            stack.append(char)

    # remove spaces
    stack = [x for x in stack if x != ' ']

    # check order of operands vs. operators and parentheses
    # also check for un-assigned variables
    for i in range(len(stack) - 1):
        if stack[i].isalnum() and stack[i+1].isalnum():
            return None
        elif stack[i] in '+-*/' and stack[i+1] in '+-*/)':
            return None
        elif stack[i][0].isalpha() and stack[i] not in variables:
            return None
    if stack[-1][0].isalpha() and stack[-1] not in variables:
        return None

    return stack


def postfix_list(infix_list):
    """
    Convert adeque list from infix to postfix postfix notation.
    :param infix_list: a deque list of an infix'd mathematical expression.
    :return: a deque list of postfix notation.
    """
    stack, postfix = deque(), deque()
    
    for op in infix_list:
        if op.isnumeric():  # operand number
            postfix.append(int(op))
        elif op.isalpha():  # operand variable
            try:
                postfix.append(variables[op])
            except KeyError:
                print(f'Unknown variable {op}')
                return None
        elif op in '+-*/':  # any operator
            try:
                if (stack[-1] == '(') or (precedence[stack[-1]] < precedence[op]):
                    stack.append(op)
                elif precedence[stack[-1]] >= precedence[op]:
                    while (precedence.get(stack[-1], 0) >= precedence[op]) or (stack[-1] != '('):
                        postfix.append(stack.pop())
                    stack.append(op)
            except IndexError:
                stack.append(op)
        elif op == '(':
            stack.append(op)
        elif op == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()

    while stack:
        postfix.append(stack.pop())

    return postfix


def calculation(expression):
    """
    Calculate a mathematical expression converted to postfix deque.
    :param expression: a deque list of a postfix'd mathematical expression.
    :return: the calculated result of the mathematical expression.
    """
    stack = deque()

    try:
        for op in expression:
            if type(op) == int:
                stack.append(op)
            elif op in '+-*/':
                num2 = stack.pop()
                num1 = stack.pop()
                if op == '+':
                    stack.append(num1 + num2)
                elif op == '-':
                    stack.append(num1 - num2)
                elif op == '*':
                    stack.append(num1 * num2)
                elif op == '/':
                    try:
                        stack.append(num1 / num2)
                    except ZeroDivisionError:
                        return 'Cannot divide by zero'
    except IndexError:
        return int(user_input)

    return int(stack[0])


def run():
    """Run this function to start the calculator."""
    repeat = True
    while repeat:
        guide()
        user_input = input()
        if user_input.startswith('/'):
            repeat = _command(user_input)
        elif '=' in user_input:
            var_assign(user_input)
        else:
            valid_brackets = validate_brackets(user_input)
            infix = infix_list(user_input)
            if valid_brackets and infix:
                result = postfix_list(infix)
                result = calculation(result)
                print(f'{user_input} = {result}')
            elif not valid_brackets:
                print('Invalid expression')
