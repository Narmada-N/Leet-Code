# from collections import deque
# from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue = deque([root])
        while(queue):
            current = queue.popleft()
            current.left, current.right =  current.right, current.left
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root