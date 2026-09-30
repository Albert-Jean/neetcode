# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        right = root.right
        if right and right.val > root.val:
            self.isValidBST(root.right)
        else:
            return False
        left = root.left
        if left and left.val < root.val:
            self.isValidBST(root.left)
        else:
            return False
        return True