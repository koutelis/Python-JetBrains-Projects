from collections import deque

# THERE IS A BUG WITH NEGATIVE INTEGERS THAT MUST BE FIXED

def guide():
    print('\nType:')
    print('====')
    print('/help')
    print('/exit')
    print('mathematical expression\n')


def help():
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


def command(string):
    if string == '/exit':
        print('\nThank you for (literally) counting on us!')
        return False
    elif string == '/help':
        help()
    else:
        print('Unknown command')
    return True


def var_assign(x):
    """populates the variables dictionary"""
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

from collections import deque


def var_assign(x):
    """populates the variables dictionary"""
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


def test_brackets(string):
    stack = deque()

    for item in string:
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


def infix_list(string):
    """takes mathematical expression in string format and returns a deque list of infix notation"""
    stack = deque()
    postfix = deque()
    if string[:2] in '+ - * / ' or string[0] in '*)':  # can't start with operator
        return False
    for char in string:
        if stack:
            # checks for number operands
            if char.isnumeric():
                if stack[-1].isnumeric():
                    stack[-1] += char
                elif stack[-1].isalpha():
                    return False
                else:
                    stack.append(char)
            # checks for var operands
            elif char.isalpha():
                if stack[-1].isalpha():
                    stack[-1] += char
                elif stack[-1].isnumeric():
                    return False
                else:
                    stack.append(char)
            elif char == ' ' and stack[-1] != ' ':
                stack.append(char)
            elif char == '(':
                if stack[-1].isalnum():
                    return False
                stack.append(char)
            elif char == ')':
                if stack[-1] in '(-+*/':
                    return False
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
                    return False
                stack.append(char)
        else:
            stack.append(char)

    # remove spaces
    stack = [x for x in stack if x != ' ']
    print(stack)

    # check order of operands vs. operators and parentheses
    for i in range(len(stack) - 1):
        if stack[i].isalnum() and stack[i+1].isalnum():
            return False
        elif stack[i] in '+-*/' and stack[i+1] in '+-*/)':
            return False

    return stack


def postfix_list(expression):
    """takes previously converted infix deque and returns a new deque list in postfix notation"""
    stack, postfix = deque(), deque()
    
    for op in expression:
        if op.isnumeric():  # operand number
            postfix.append(int(op))
        elif op.isalpha():  # operand variable
            try:
                postfix.append(variables[op])
            except KeyError:
                print(f'Unknown variable {op}')
                return
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
    """takes previously converted postfix deque and returns the result"""
    result = 0
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


# init
variables = {}
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
repeat = True

while repeat:
    guide()
    user_input = input()

    if user_input.startswith('/'):
        repeat = command(user_input)
    elif '=' in user_input:
        var_assign(user_input)
    else:
        brackets = test_brackets(user_input)
        infix = infix_list(user_input)
        if brackets and infix:
            result = postfix_list(infix)
            result = calculation(result)
            print(result)
        elif not brackets:
            print('Invalid expression')
