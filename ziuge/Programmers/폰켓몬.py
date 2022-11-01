# Lv. 2
# 폰켓몬
def solution(nums):
    answer = 0

    if len(nums) // 2 > len(set(nums)) :
        answer = len(set(nums))
    else: 
        answer = len(nums) // 2

    return answer

# 간결한 풀이
def solution(nums):
    return min(len(nums) / 2, len(set(nums)))
