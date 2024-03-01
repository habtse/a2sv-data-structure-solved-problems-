class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
      grid = [[0]*n for _ in range(m)]
      for x, y in guards:
        grid[x][y] = 'G'
      for x, y in walls:
        grid[x][y] = 'W'
        
      grid2 = [[0]*n for _ in range(m)]
      for x, y in guards:
        grid2[x][y] = 'G'
      for x, y in walls:
        grid2[x][y] = 'W'
        
      for i in range(m):
        cache = []
        has_G = False
        for j in range(n):
          if grid[i][j] == 0:
            cache.append(j)
          elif grid[i][j] == 'G':
            if cache:
              for k in cache:
                grid[i][k] = 'O'
              cache = []
            has_G = True
          else:
            if has_G:
              if cache:
                for k in cache:
                  grid[i][k] = 'O'
                  cache = []
              has_G = False
            else:
              cache = []
        if cache:
          if has_G:
            for k in cache:
                grid[i][k] = 'O'
      
      for j in range(n):
        cache = []
        has_G = False
        for i in range(m):
          if grid2[i][j] == 0:
            cache.append(i)
          elif grid2[i][j] == 'G':
            if cache:
              for k in cache:
                grid2[k][j] = 'O'
              cache = []
            has_G = True
          else:
            if has_G:
              if cache:
                for k in cache:
                  grid2[k][j] = 'O'
                  cache = []
              has_G = False
            else:
              cache = []
        if cache:
          if has_G:
            for k in cache:
                grid2[k][j] = 'O'
      
      res = 0
      for i in range(m):
        for j in range(n):
          if grid[i][j] == 0 and grid2[i][j] == 0: res += 1
      return res
        