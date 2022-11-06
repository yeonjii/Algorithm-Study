# LeetCode - Next Permutation
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        # 최초로 오른쪽 값이 커지는 index 찾기
        index = len(nums) - 1
        while index > 0 and nums[index-1]>=nums[index]:
            index -= 1
        
        # index 이후 값 연쇄적으로 swap
        if index == 0: 
            nums.reverse()
            return
        else: 
            i = index - 1
            for j in range(len(nums)-1, i, -1):
                if nums[j]>nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    break
            nums[i+1:] = nums[i+1:][::-1]
        return
      
# LeetCode - Search in Rotated Sorted Array
## Sol1
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 가장 작은 값의 index 찾기
        index = nums.index(min(nums))

        # target 찾기
        left, right = 0, len(nums) - 1
        while left <= right :
            mid = (left + right) // 2
            mid_value = (index + mid) % len(nums)

            if nums[mid_value] == target :
                return mid_value
            elif nums[mid_value] < target :
                left = mid + 1
            else:
                right = mid - 1

        return -1 

## Sol2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums: 
            return nums.index(target)
        else: 
            return -1
          

# LeetCode - Validate Binary Search Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isValidBST(self, root):
        return self.recursive(root, None, None)

    def recursive(self, root, min, max):
        if not root:
            return True
        elif (min is not None and min >= root.val) or (max is not None and max <= root.val):
            return False
        else:
            return self.recursive(root.left, min, root.val) and self.recursive(root.right, root.val, max)
