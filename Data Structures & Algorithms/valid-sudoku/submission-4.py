class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row by row
        length = len(board)
        for row in range(length):
            set_row = set()
            for column in range(len(board)):
                if board[row][column] == ".":
                    continue
                if board[row][column] not in set_row:
                    set_row.add(board[row][column])
                else:
                    return False
       
        #check column by column
        for row in range(length):
            set_column = set()
            for column in range(len(board)):
                if board[column][row] == ".":
                    continue
                if board[column][row] not in set_column:
                    set_column.add(board[column][row])
                else:
                    return False
        
        #check 3x3 blocks
        diction = {key: set() for key in [0, 1, 2, 3, 4, 5, 6, 7, 8]}
        for row in range(length):
            for column in range(length):
                if board[row][column] == ".":
                    continue
                if board[row][column] not in diction[(row // 3) * 3 + (column // 3)]:
                    diction[(row // 3) * 3 + (column // 3)].add(board[row][column])
                else:
                    return False
        return True
            