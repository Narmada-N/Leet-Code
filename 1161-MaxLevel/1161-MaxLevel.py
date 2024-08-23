# from typing import Optional
# from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max_sum = float(-inf)
        level = 1
        max_level = 1 
        current_level = 1
        while queue:
            level_len = len(queue)
            sum=0
            for _ in range(level_len):
                node = queue.popleft()
                sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if sum>max_sum:
                max_sum= sum
                max_level = current_level
            current_level+=1
        return max_level