# sol1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i]+nums[j]:
                    return [i,j]

# Runtime: 3863 ms, faster than 18.13% of Python3 online submissions for Two Sum.
# Memory Usage: 14.9 MB, less than 96.05% of Python3 online submissions for Two Sum.



# sol2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}  # {val:idx}
        for idx, val in enumerate(nums):
            diff = target-val
            if diff in check:
                return [check[diff], idx]
            else:
                check[val] = idx

# Runtime: 134 ms, faster than 54.10% of Python3 online submissions for Two Sum.
# Memory Usage: 15.1 MB, less than 68.63% of Python3 online submissions for Two Sum.