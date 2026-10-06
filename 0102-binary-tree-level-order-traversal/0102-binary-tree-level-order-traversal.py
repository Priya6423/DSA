# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        d=deque([root])
        ans=[]
        answer=[]
        while d:
            level=len(d)
            while level:
                node=d.popleft()
                ans.append(node.val)
                if node.left: d.append(node.left)
                if node.right: d.append(node.right)
                level-=1
            answer.append(ans)
            ans=[]
        return answer
