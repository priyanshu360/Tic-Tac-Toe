"""
# Tic Tac Toe Player
"""
import copy 
import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
	
	count_X = 0
	count_O = 0

	for row in board:
		for column in row:
			if column == X:
				count_X += 1
			if column == O:
				count_O += 1
				
	if count_X > count_O:
		return O
	else:
		return X
		
	raise NotImplementedError


def actions(board):
	
	possibleActions = set()
	
	for i in range(0, 3):
		for j in range(0, 3):
			if board[i][j] == EMPTY:
				possibleActions.add((i, j))
	
	return possibleActions
	
	raise NotImplementedError


def result(board, action):
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = player(board)
    return newBoard
    raise NotImplementedError


def winner(board):
	
	for i in range(0, 3):
		if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
			if board[i][0] == X:
				return X
			elif board[i][1] == O:
				return O
	
		if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
			if board[0][i] == X:
				return X
			elif board[0][i] == O:
				return O
	
	if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		if board[0][0] == X:
			return X
		elif board[0][0] == O:
			return O
	
	if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
		if board[0][2] == X:
			return X
		elif board[0][2] == O:
			return O
			
	return None
	raise NotImplementedError


def terminal(board):
	
	if winner(board) != None:
		return True
	
	if len(actions(board)) == 0:
		return True
	
	return False
	raise NotImplementedError


def utility(board):
	
	if winner(board) == X:
		return 1
	
	elif winner(board) == O:
		return -1
	
	return 0
	raise NotImplementedError


def minimax(board):
	
	favMove = tuple()
	if(player(board) == X):
		maxUtil = -10000000000000000
	
		for action in actions(board):
			tempBoard = result(board, action)
			curUtil = findUtil(tempBoard)
			if(maxUtil <= curUtil):
				favMove = action
				maxUtil = curUtil
	
	if(player(board) == O):
		minUtil = 100000000000000000
		
		for action in actions(board):
			tempBoard = result(board, action)
			curUtil = findUtil(tempBoard)
			if(minUtil >= curUtil):
				favMove = action
				minUtil = curUtil
	
	# print(favMove)
	return favMove
	raise NotImplementedError

store_util = {}

def findUtil(board):
	if(terminal(board)):
		return utility(board)
	
	if store_util.get(str(board)) != None:
		return store_util.get(str(board))
	
	if(player(board) == X):
		maxUtil = -10000000000000000
		
		for action in actions(board):
			tempBoard = result(board, action)
			maxUtil = max(maxUtil, findUtil(tempBoard))
			store_util[str(board)] = maxUtil
		return maxUtil
		
	if(player(board) == O):
		minUtil = 100000000000000000
		
		for action in actions(board):
			tempBoard = result(board, action)
			minUtil = min(minUtil, findUtil(tempBoard))
			store_util[str(board)] = minUtil
		return minUtil
