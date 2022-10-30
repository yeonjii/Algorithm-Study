nums = [0,1,0,3,12]

# 투포인터 풀이
zero = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[zero], nums[i] = nums[i], nums[zero]
        zero += 1

# Runtime: 168 ms, faster than 95.81% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.7 MB, less than 17.22% of Python3 online submissions for Move Zeroes.