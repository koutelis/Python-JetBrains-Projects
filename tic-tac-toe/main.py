from tictactoe import TicTacToe


if __name__ == "__main__":
    introduction = '''Welcome to a game of Tic Tac Toe!
You need two players to play, each can input two numbered coordinates (1-3).
1st coordinate is on the x-axis
2nd coordinate is on the y-axis
Good luck!
'''
    print(introduction)
    TicTacToe().play()
