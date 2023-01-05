# LeetCode - Zigzag Conversion 
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = [""] * numRows

        # 방향
        DOWN, UP = 1, -1
        direction = 0

        # 인덱스 (라인)
        START, END = 0, numRows - 1
        index = 0

        # 인덱스 별 저장
        for s_item in s:
            answer[index] += s_item

            if index == END:
                direction = UP
            elif index == START :
                direction = DOWN

            index += direction 

        return "".join(answer)
      
# LeetCode - Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left, right = 0, len(height) - 1

        while left < right :
            # Water 사각형 업데이트
            min_height = min(height[left],height[right])
            curr = (right - left) * min_height
            answer = max(answer, curr)

            # 다음 left
            while height[left] <= min_height:
                left += 1
                if left >= len(height):
                    break

            # 다음 right
            while height[right] <= min_height:
                right -= 1
                if right < 0:
                    break

        return answer
      
# Programmers - 파괴 되지 않은 건물
def solution(board, skill):
    answer = 0
    
    N, M = len(board[0]), len(board)
    cum_sum = [[0] * (N + 1) for _ in range(M + 1)] 
    
    # 누적합
    for t, r1, c1, r2, c2, degree in skill:
        cum_sum[r1][c1] += degree if t == 2 else -degree
        cum_sum[r1][c2 + 1] += -degree if t == 2 else degree
        cum_sum[r2 + 1][c1] += -degree if t == 2 else degree
        cum_sum[r2 + 1][c2 + 1] += degree if t == 2 else -degree
        
    # 누적합 - 행
    for i in range(len(cum_sum) - 1):
        for j in range(len(cum_sum[0]) - 1):
            cum_sum[i][j + 1] += cum_sum[i][j]
    
    # 누적합 - 열
    for j in range(len(cum_sum[0]) - 1):
        for i in range(len(cum_sum) - 1):
            cum_sum[i + 1][j] += cum_sum[i][j]
    
    # 답
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += cum_sum[i][j]
            if board[i][j] > 0: answer += 1
    
    return answer
