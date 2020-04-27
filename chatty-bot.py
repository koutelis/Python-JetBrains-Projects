from random import choice

def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + ' by HB.\n')

def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!\n')

def guess_age():
    print('Let me guess your age.')
    rem3 = int(input('Divide your age by 3, what is the remainder?'))
    rem5 = int(input('Divide your age by 5, what is the remainder?'))
    rem7 = int(input('Divide your age by 7, what is the remainder?'))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("\nYour age is " + str(age) + "; that's a good time to start programming!\n")

def count():
    print('Now I will prove to you that I can count to any number you want.\n')
    num = int(input('Enter max number: '))
    for i in range(num + 1):
        print(i, '!')
    print()

def test(question):
    print("\nLet's test your programming knowledge:\n")
    test = choice(list(question.keys()))
    print(f'{test} ?')
    input('(Press a key to continue...)\n')
    if len(question[test]) > 1:
    	print(question[test])
    else:
    	# if question has multiple answers
	    for i in range(0, len(question[test])):
	        print(f'{i + 1}. {question[test][i]}')

def end():
    print('\nCongratulations, have a nice day!')

# Programming questions and answers. Add more in the form of dictionary
q_and_a = {'Why do we use methods': ['To repeat a statement multiple times.', 'To decompose a program into several small subroutines.', 
'To determine the execution time of a program.', 'To interrupt the execution of a program.'], 'Who created Python': ['Guido van Rossum']}

# main
greet('Ash 2X3ZB9CY', '2013')
remind_name()
guess_age()
count()
test(q_and_a)
end()
