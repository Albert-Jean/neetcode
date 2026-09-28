# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #base case root has p and q --> return root
        #search for p and q in each tree -> recursion
        if not root or not p or not q :
            return None
        if max(q.val,p.val) < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif min(q.val,p.val) > root.val:
            return self.lowestCommonAncestor(root.right,p,q)        
        else :
            return root
