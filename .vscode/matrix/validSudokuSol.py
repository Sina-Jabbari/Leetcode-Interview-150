class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            rowselect = [0] * 9
            colselect = [0] * 9
            boxselect = [0] * 9

            for j in range(9):
                cell = board[i][j]
                colcell = board[j][i]

                #row check
                if cell != ".": 
                    if rowselect[int(cell)-1] > 0:
                        return False
                    rowselect[int(cell)-1] += 1
                
                #col check
                if colcell != ".":
                    if colselect[int(colcell)-1] > 0:
                        return False
                    colselect[int(colcell)-1] += 1

                #box check
                rowIndex = 3 * (i // 3)
                colIndex = 3 * (i % 3)
                boxcell = board[rowIndex + j // 3][colIndex + j % 3]
                if boxcell != '.':
                    if boxselect[int(boxcell) - 1] > 0:
                        return False
                    boxselect[int(boxcell) - 1] += 1

        return True