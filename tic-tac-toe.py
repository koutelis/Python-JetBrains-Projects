# Tic-Tac-Toe game

def board(xo):
	print('---------')
	print('| {} {} {} |'.format(xo[0], xo[1], xo[2]))
	print('| {} {} {} |'.format(xo[3], xo[4], xo[5]))
	print('| {} {} {} |'.format(xo[6], xo[7], xo[8]))
	print('---------')

def player_move():
	slots = {(1, 1): 6, (1, 2): 3, (1, 3): 0, (2, 1): 7, (2, 2): 4, (2, 3): 1, (3, 1): 8, (3, 2): 5, (3, 3): 2}
	while True:
		while True:
			coordinates = input('Enter the coordinates: ').split()
			try:
				for i in range(len(coordinates)):
					coordinates[i] = int(coordinates[i])
				break
			except:
				print('You should enter numbers!')

		if (len(coordinates) != 2) or (max(coordinates) > 3) or (min(coordinates) < 1):
			print('Coordinates should be from 1 to 3!')
		else:
			coordinates = tuple(coordinates)
			break
	return slots[coordinates]

def win_check(xo, player):
	# check rows
	if any([(player == xo[0] == xo[1] == xo[2]), (player == xo[3] == xo[4] == xo[5]), (player == xo[6] == xo[7] == xo[8])]):
		return True
	# check cols
	elif any([(player == xo[0] == xo[3] == xo[6]), (player == xo[1] == xo[4] == xo[7]), (player == xo[2] == xo[5] == xo[8])]):
		return True
	# check diag
	elif any([(player == xo[0] == xo[4] == xo[8]), (player == xo[2] == xo[4] == xo[6])]):
		return True
	return False

def switch_player(x_or_o):
	if x_or_o == 'X':
		return 'O'
	else:
		return 'X'


# init
board_state = [' ' for i in range(9)]
current_player = 'X'

# show
board(board_state)

# start
while True:
	# player move
	print('Coordinates: numbers 1-3 for x-axis and y-axis, separated by space')
	while True:
		move = player_move()
		if board_state[move] == ' ':
			board_state[move] = current_player
			break
		else:
			print('This cell is occupied! Choose another one!')

	# show
	board(board_state)

	# winning conditions
	if win_check(board_state, current_player):
		print(f'{current_player} wins')
		break
	elif ' ' not in board_state:
		print('Draw')
		break

	# switch player
	current_player = switch_player(current_player)
