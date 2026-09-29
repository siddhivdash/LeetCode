# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        left_to_right = True 
        while q:
            levels = []
            for i in range(len(q)):
                node = q.popleft()
                levels.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not left_to_right:
                levels.reverse()
            res.append(levels)
            left_to_right = not left_to_right
        return res

        