# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
        dfs(root)
        return result[k-1]