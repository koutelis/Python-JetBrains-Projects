

class TicTacToe:

	slots = {(1, 1): 6, (1, 2): 3, (1, 3): 0, (2, 1): 7, (2, 2): 4, (2, 3): 1, (3, 1): 8, (3, 2): 5, (3, 3): 2}

	def __init__(self):
		self.xo = ['.' for i in range(9)]
		self.current_player = 'X'
	
	def __str__(self):
		output = '---------\n'
		for i in range(3):
			output += f"| {' '.join(self.xo[i*3:i*3+3])} |\n"
		output += '---------\n'
		return output
	
	def __make_move(self):
		"""A player makes a move."""
		while True:
			cell = self.__input_coordinates()
			if self.xo[cell] == '.':
				self.xo[cell] = self.current_player
				return
			else:
				print('This cell is occupied! Choose another one!')

	def __input_coordinates(self):
		"""
		Helper of __make_move(). Receive coordinates from player (user).
		:return: a valid tuple of coordinates (x, y)
		"""
		print('Coordinates: numbers 1-3 for x-axis and y-axis, separated by space')
		while True:
			try:
				coordinates = tuple(map(int, input(f"Enter the coordinates for '{self.current_player}': ").split()))
			except ValueError:
				print('You should enter numbers!')
			if (len(coordinates) != 2) or (max(coordinates) > 3) or (min(coordinates) < 1):
				print('Coordinates should be from 1 to 3!')
			else:
				return TicTacToe.slots[coordinates]

	def __win_check(self):
		"""
		Check if there is a winner
		:return: True if a player wins, else False
		"""
		rows_check = any([all([self.current_player == slot for slot in self.xo[i:i+3]]) for i in range(0, 9, 3)])
		if rows_check: return True

		cols_check = any([all([self.current_player == slot for slot in self.xo[i::3]]) for i in range(3)])
		if cols_check: return True

		diags_check = any([all([self.current_player == slot for slot in self.xo[0:9:4]]),
						   all([self.current_player == slot for slot in self.xo[2:7:2]])])
		if diags_check: return True
		return False
	
	def __draw_check(self):
		"""
		Check if the game ends in draw.
		:return: True if all slots are occupied, else False.
		"""
		if '.' not in self.xo:
			return True
		return False

	def __switch_player(self):
		"""Current player swap"""
		self.current_player = 'O' if self.current_player == 'X' else 'X'
	
	def play(self):
		"""Run this function to start the game."""
		print(self)
		while True:
			self.__make_move()
			print(self)
			# winning conditions
			if self.__win_check():
				print(f'{self.current_player} wins')
				break
			elif self.__draw_check():
				print('Draw')
				break
			self.__switch_player()
