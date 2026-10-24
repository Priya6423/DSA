# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        index_of={}
        for i in range(len(inorder)):
            index_of[inorder[i]]=i
        post_index=len(inorder)-1
        def helper(left,right):
            nonlocal post_index
            if left>right:
                return None
            root_val=postorder[post_index]
            post_index-=1
            root=TreeNode(root_val)
            mid=index_of[root_val]
            root.right=helper(mid+1,right)
            root.left=helper(left,mid-1)
            return root
        return helper(0,len(inorder)-1)
