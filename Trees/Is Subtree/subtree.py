# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False
        

        def isSameTree(root, subRoot):
            if (root and not subRoot) or (not root and subRoot):
                return False

            if not root and not subRoot:
                return True

            if root.val == subRoot.val:
                return isSameTree(root.left,subRoot.left) and isSameTree(root.right,subRoot.right)

            return False

        def dfs(root):
            if not root:
                return False

            if isSameTree(root, subRoot):
                return True
            
            return dfs(root.left) or dfs(root.right)
                

        return dfs(root)
