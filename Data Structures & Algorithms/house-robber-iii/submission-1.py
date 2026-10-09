# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #case with root and without root 
        def dfs (root)->List[int]:
            if not root:
                return [0,0]
            rightPair = dfs(root.right)
            leftPair = dfs(root.left)
            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair)+ max(rightPair)
            return [withRoot,withoutRoot]
        return max(dfs(root))
            
        