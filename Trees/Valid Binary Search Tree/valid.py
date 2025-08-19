# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validDfs(lower_bound, root, upper_bound):
            if not root:
                return True

            if not(lower_bound < root.val < upper_bound):
                return False

            left = validDfs(lower_bound, root.left, root.val)
            right = validDfs(root.val, root.right, upper_bound)

            return left and right

        return validDfs(-float('inf'), root, float('inf'))