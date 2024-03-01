class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        def inBound(i, j):
            return 0<= i < len(board) and 0 <= j < len(board[0])


        def backtrack(board, index, coord):
            nonlocal word
            if index >= len(word):
                return True
            i, j = coord
            if not inBound(i, j): return False

            if word[index] == board[i][j]:
                board[i][j] = '0'
                dir_ = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy  in dir_:
                    new_i, new_j = i+dx, j+dy
                    if backtrack(board, index+1, [new_i, new_j]):
                        return True
                board[i][j] = word[index]
            
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
              if backtrack(board, 0, [i, j]):
                  return True
        return False

            

        