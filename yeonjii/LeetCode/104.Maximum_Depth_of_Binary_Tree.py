# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(tree, i):
            if tree.left:
                dfs(tree.left, i + 1)
            if tree.right:
                dfs(tree.right, i + 1)
            if tree.left is None and tree.right is None:  # 마지막노드
                res.append(i)

        if root is None:
            res.append(0)
        else:
            dfs(root, 1)

        return max(res)