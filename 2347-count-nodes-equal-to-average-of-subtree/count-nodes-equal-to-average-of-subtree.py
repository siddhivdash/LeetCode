# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0,0
            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)

            curr_sum = left_sum + right_sum + node.val
            curr_cnt = left_cnt + right_cnt + 1
            if node.val == curr_sum // curr_cnt:
                self.ans += 1
            return (curr_sum, curr_cnt)
        dfs(root)
        return self.ans
