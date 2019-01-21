# Sonali Singh
# Monte Carlo Tic Tac Toe Simulation
# 1/21/19
import random as r
from collections import Counter
import matplotlib.pyplot as plt

# initialize tic tac toe board
board = []
# create list that will store the start positions of every game that is won (1s win)
win_start_pos = []

# create 2d board 
for x in range(3):
	space = [0]*3
	board.append(space)

# code for one tic tac toe game
def play():
	# win becomes True if player places 3 in a row
	win = False
	# the two players are -1 and 1, team keeps track of what player is putting something down, 1 always starts
	team = 1
	# turn dictates whether it is 1s turn or -1s turn.
	turn = True
	# ensures that only first move is stored
	firstmove = True

	# nine moves for board to be filled
	for move in range(9):
		# generate random place to put down move
		row = r.randrange(0,3,1)
		col = r.randrange(0,3,1)

		# store first move and then make first move = false
		if firstmove:
			pos_row = row
			pos_col = col
		firstmove = not firstmove

		# if space chosen is not empty, choose new space to play
		while board[row][col] != 0:
			row = r.randrange(0,3,1)
			col = r.randrange(0,3,1)

		# game always starts with 1's move
		if turn:
			team = 1
		else:
			team = -1

		# place 1 or -1 at specified space
		board[row][col] = team

		# if 3 in a row (1s) then game over
		if gameover() == 3:
			win = True
			break
		
		# else other team's turn
		turn = not turn

	# if game is won, append start position to list
	if win:
		win_start_pos.append((pos_row,pos_col))

	# reset the game board
	for row in range(3):
		for col in range(3):
			board[row][col] = 0

# checks if game is over and 1 wins (only tracking 1 team's wins to get data)
def gameover():
	# looks for three "1s" in a row/column/diagonal by summing values 
	row_sum0 = board[0][0]+board[0][1]+board[0][2]
	row_sum1 = board[1][0]+board[1][1]+board[1][2]
	row_sum2 = board[2][0]+board[2][1]+board[2][2]
	col_sum0 = board[0][0]+board[1][0]+board[2][0]
	col_sum1 = board[0][1]+board[1][1]+board[2][1]
	col_sum2 = board[0][2]+board[1][2]+board[2][2]
	diag_sum1 = board[0][0]+board[1][1]+board[2][2]
	diag_sum2 = board[2][0]+board[1][1]+board[0][2]

	# appends sums of all the row/columns/diagonals to list
	sums = [row_sum0, row_sum1, row_sum2, col_sum0, col_sum1, col_sum2, diag_sum1, diag_sum2]
	
	# look through list to find '3's meaning that 1 would have three in a row
	for element in sums:
		if element == 3:
			# when element = 3, game is won
			return element
	return 0


# show tic tac toe board (call function to test)
def print_board():
	for y in range(3):
		for x in range(3):
			print(board[y][x],end=" ")
		print("")

# run game many times to see proper distribution of results
for x in range(100000):
	play()

# occurrences of winning starting positions are sorted
results = sorted(Counter(win_start_pos).items())

# contains occurrences that game was won on specified starting position
y_data = []
# stores tuple of starting position (row,col)
x_data = []

# appending data to respective list
for tuples in results:
	y_data.append(tuples[1])
	x_data.append(tuples[0])

# final list of wins per each starting point
print(results)

# OMH: Sonali Singh