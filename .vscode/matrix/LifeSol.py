class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """ 
        newboard = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]
        #len(board) = len(row)
        #len(board[0]) = len(col)
        for m in range(len(board)):
            for n in range(len(board[0])): 
                liveneighbours = 0

                #counting liveneighbours per cell
                #check all 8 cases around a cell if its not out of index range
                if m > 0 and n > 0:
                    if board[m-1][n-1] == 1:
                        liveneighbours += 1
                if m > 0:
                    if board[m-1][n] == 1:
                        liveneighbours += 1
                if m > 0 and n < len(board[0]) - 1:
                    if board[m-1][n+1] == 1:
                        liveneighbours += 1
                if n > 0:
                    if board[m][n-1] == 1:
                        liveneighbours += 1
                if n < len(board[0]) - 1:
                    if board[m][n+1] == 1:
                        liveneighbours += 1
                if m < len(board) - 1 and n > 0:
                    if board[m+1][n-1] == 1:
                        liveneighbours += 1
                if m < len(board) - 1:
                    if board[m+1][n] == 1:
                        liveneighbours += 1
                if m < len(board) - 1 and n < len(board[0]) - 1:
                    if board[m+1][n+1] == 1:
                        liveneighbours += 1

                #cop the new board based on the rules
                if board[m][n] == 1:
                    #under-population
                    if liveneighbours < 2:
                        newboard[m][n] = 0  
                    
                    #next generation
                    elif liveneighbours <= 3:
                        newboard[m][n] = 1  

                    #over-population
                    else:
                        newboard[m][n] = 0 

                #reproduction
                elif board[m][n] == 0 and liveneighbours == 3:
                    newboard[m][n] = 1  
        #paste copy of board into board
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = newboard[i][j]

