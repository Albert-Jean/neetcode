"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        #init value
        new = {}
        new[node] = Node(node.val)
        queue = deque([node])
        #running bfs
        while queue:
            curr = queue.popleft()
            for neighbors in curr.neighbors:
                if neighbors not in new:
                    new[neighbors] = Node(neighbors.val)
                    queue.append(neighbors)
                new[curr].neighbors.append(new[neighbors])
        return new[node]


