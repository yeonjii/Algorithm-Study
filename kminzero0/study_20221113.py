# LeetCode Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []

        while True:
            if len(matrix) == 0 :
                break

            answer.extend(matrix[0])
            matrix.remove(matrix[0])
            matrix = list(map(list, zip(*matrix)))[::-1]
        
        return answer        
 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []

        # 위치 (왼, 오, 위, 아래)
        left, right, up, down = 0, len(matrix[0]), 0, len(matrix)

        while left < right and up < down:
            # 왼쪽 -> 오른쪽
            for i in range(left, right):
                answer.append(matrix[up][i])
            up += 1

            # 위쪽 -> 아래쪽
            for i in range(up, down):
                answer.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and up < down):
                break

            # 오른쪽 -> 왼쪽
            for i in range(right - 1, left - 1, -1):
                answer.append(matrix[down - 1][i])
            down -= 1

            # 아래쪽 -> 위쪽
            for i in range(down - 1, up - 1, -1):
                answer.append(matrix[i][left])
            left += 1
            
        return answer
      
      
      
# LeetCode Spiral Matrix II
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:        
        answer = [[0]*n for _ in range(n)]
        
        left, right, up, down = 0, n-1, 0, n-1
        mid = n//2 
        val = 1
        
        while True:
            if val > n**2:
                break
            
            if up == right:
                answer[mid][mid] = val
                break

            for i in range(left, right):
                answer[up][i] = val
                val += 1

            for i in range(up, down):
                answer[i][right] = val
                val += 1

            for i in range(right, left, -1):
                answer[down][i] = val
                val += 1

            for i in range(down, up, -1):
                answer[i][left] = val
                val += 1

            left += 1; right -= 1; up += 1; down -= 1;

        return answer


# LeetCode - Word Search
class Solution:  
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        visited = set() 
        
        def dfs(r, c, w):
            if w == len(word):
                return True
            if r < 0 or c < 0 or r >= M or c >= N:
                return False
            if word[w] != board[r][c]:
                return False
            if (r,c) in visited:
                return False
            
            visited.add((r,c))
            answer = dfs(r+1,c,w+1) or dfs(r-1,c,w+1) or dfs(r,c+1,w+1) or dfs(r,c-1,w+1)
            visited.remove((r,c))

            return answer
        
        #### 시간초과 방지 ###
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        ########################

        for r in range(M):
            for c in range(N):
                if board[r][c] == word[0]:
                    if dfs(r,c,0): 
                        return True
        return False
