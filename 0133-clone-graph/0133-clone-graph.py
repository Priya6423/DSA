"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones={}
        def dfs(orig_node):
            if orig_node in clones:
                return clones[orig_node]
            clone=Node(val=orig_node.val,neighbors=[])
            clones[orig_node]=clone
            for nb in orig_node.neighbors:
                clone.neighbors.append(dfs(nb))
            return clone
        return dfs(node)
        