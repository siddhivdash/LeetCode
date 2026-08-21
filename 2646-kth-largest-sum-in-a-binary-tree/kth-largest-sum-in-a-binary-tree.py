# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        q = deque([root])
        res = []
        
        while q:
            summ = 0 
            for _ in range(len(q)):
                node = q.popleft()
                summ += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(summ)
        if len(res) < k:
            return -1
        res.sort(reverse = True)
        return res[k - 1]
