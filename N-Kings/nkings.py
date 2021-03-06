# Creates the board and keeps all the positions open.
def createBoard(N):
	board = {}
	for i in range(N):
		board[i] = [0 for j in range(N)]
	return board

#Sets the board, places all the peices. 1 - King, 2 - Invalid position, 0 - Open position
def setBoard(K, N, pos):
	board = createBoard(N)
	for i in range(K):
		# Excluding the diagonal blocks from the current position.
		if i-1 >= 0:
			board[i-1][pos[i]] = 2
			if pos[i] - 1 >= 0:
				board[i-1][pos[i] - 1] = 2
				
			if pos[i] + 1 <= N-1:
				board[i-1][pos[i] + 1] = 2
		if i+1 <= N-1:
			board[i+1][pos[i]] = 2
			if pos[i] - 1 >= 0:
				board[i+1][pos[i] - 1] = 2
			if pos[i] + 1 <= N-1:
				board[i+1][pos[i] + 1] = 2
		if pos[i] - 1 >= 0:
			board[i][pos[i] - 1] = 2
		if pos[i] + 1 <= N-1:
			board[i][pos[i] + 1] = 2
			
		# Excluding the rows and column in which current block lies.
		for j in range(N):
			board[i][j] = 2
			board[j][pos[i]] = 2
		board[i][pos[i]] = 1	

	return board

# Tells if the position we are currently in is valid or not.
def isPosValid(board, i, j, N):
	if board[i][j] == 2:
		return False
	return True

# Displays the chess board.
def display(board, N):
	print "---------Start-------- \n"
	for i in range(N):
		for j in range(N):
			print board[i][j], " ",
		print "\n"
	print "---------End-------- \n"
		
# Places the peice on the board using setBoard.
def placePiece(board, N, K, newpos):
	if K == N:
		return 1
	else:
		solved = 0
		for j in range(N):
			if isPosValid(board, K, j, N):
				K += 1
				newpos.append(j)
				preboard = board
				board = setBoard(K, N, newpos)
				solved += placePiece(board, N, K, newpos)
				newpos.pop()
				K -= 1
				board = setBoard(K, N, newpos)
		return solved

# Main calls it solve the problem.
def solve(N, K, pos):
	solutions = []
	board = setBoard(K, N, pos)
	# display(board, N)
	solutions = placePiece(board, N, K, pos)
	print(solutions%1000000007)
	
# Main.
if __name__ == '__main__':
	T = int(raw_input())
	for i in range(T):
		pos = []
		NK = raw_input()
		N = int(NK.split()[0])
		K = int(NK.split()[1])
		if K > 0:
			lis = raw_input().split()
			pos = [int(l) for l in lis]
		else:
			raw_input()
		solve(N, K, pos)
