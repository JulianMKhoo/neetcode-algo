class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        col_check = {}
        row_check = {}
        block_check = {}

        for row in range(n):
            col_len = len(board[row])
            for col in range(col_len):
                if row not in col_check:
                    if board[col][row] != ".":
                        col_check[row] = [board[col][row]]
                else:
                    if board[col][row] in col_check[row]:
                        return False
                    if board[col][row] != ".":
                        col_check[row].append(board[col][row])
                if board[row][col] == ".":
                    continue


                if row not in row_check:
                    row_check[row] = [board[row][col]]
                else:
                    if board[row][col] in row_check[row]:
                        return False
                    row_check[row].append(board[row][col])

                index = (row // 3) * 3 + (col // 3)

                if index not in block_check:
                    block_check[index] = [board[row][col]]
                else:
                    if board[row][col] in block_check[index]:
                        return False
                    block_check[index].append(board[row][col])
        return True