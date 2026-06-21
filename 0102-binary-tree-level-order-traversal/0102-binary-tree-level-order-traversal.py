# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        answer=[]
        ans=[]
        queue=deque([root])
        while queue:
            level=len(queue)
            for i in range(level):
                node=queue.popleft()
                answer.append(node.val)
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            ans.append(answer)
            answer=[]
        return ans


        