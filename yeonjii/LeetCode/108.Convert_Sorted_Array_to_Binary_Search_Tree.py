# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            if len(nums)==0:
                return None
            mid = nums[len(nums)//2]
            root = TreeNode(mid)
            root.left = dfs(nums[:len(nums)//2])
            root.right = dfs(nums[len(nums)//2+1:])
            return root
        return dfs(nums)
