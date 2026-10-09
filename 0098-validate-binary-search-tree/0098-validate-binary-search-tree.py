# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        low=float('-inf')
        high=float('inf')
        def helper(node,low,high):
            if not node:
                return True
            if node.val<=low or node.val>=high:
                return False    
            return helper(node.left,low,node.val) and helper(node.right,node.val,high)
            
            
        return helper(root,low,high)
       
        


        