class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            row, col, sq = set(), set(), set()
            for c in range(9):
                if board[r][c] != "." and board[r][c] not in col: 
                    col.add(board[r][c])
                elif board[r][c] != "." and board[r][c] in col:
                    return False
                if board[c][r] != "." and board[c][r] not in row:
                    row.add(board[c][r]) 
                elif board[c][r] != "."and board[c][r] in row:
                    return False 
            
        for r in range(0, 9, 3): 
            for c in range(0, 9, 3): 
                s = board[c][r:r+3] + board[c+1][r:r+3] + board[c+2][r:r+3]
                square = set()

                for n in s:
                    if n in square:
                        return False
                    elif n != ".":
                        square.add(n)
                
        return True