class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix)
        col_len = len(matrix[0])
        up, down = 0, row_len -1
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        while up < down:
            mid = up + ((down - up)//2)
            if matrix[mid][0]== target or matrix[mid][-1]== target:
                return True
            elif matrix[mid][0] < target and target < matrix[mid][-1]:
                low, high = 0, col_len -1
                while low < high:
                    col_mid = low + ((high - low)//2)
                    if matrix[mid][col_mid] < target:
                        low = col_mid + 1
                    elif matrix[mid][col_mid] > target:
                        high  = col_mid
                    else:
                        return True
                return False
            if matrix[mid][-1] > target:
                down = mid
            elif  matrix[mid][-1] < target:
                up = mid + 1
        
        if matrix[up][0]== target or matrix[up][-1]== target:
            return True
        elif matrix[up][0] < target and target < matrix[up][-1]:
            low, high = 0, col_len -1
            while low < high:
                col_mid = low + ((high - low)//2)
                if matrix[up][col_mid] < target:
                    low = col_mid + 1
                elif matrix[up][col_mid] > target:
                    high  = col_mid
                else:
                    return True
            return False
    