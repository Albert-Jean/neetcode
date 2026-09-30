# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = root
        resR,resL = 1,1
        if not root:
            return 0
        while curr:
            curr = curr.right
            resR+=1
        curr = root
        while curr:
            curr = curr.left
            resL+=1
        return max(resR,resL)


        