# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        summ=0
        def helper(node,ts,summ):
            if not node:
                return False
            if not node.left and not node.right and summ+node.val==ts:
                return True
            return helper(node.left,ts,summ+node.val) or helper(node.right,ts,summ+node.val)
        return helper(root,targetSum,summ)
            


        