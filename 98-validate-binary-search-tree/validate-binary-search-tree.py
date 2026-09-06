# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def lauda(root, minn, maxx):
            if not root:
                return True
            if not (minn < root.val < maxx):
                return False
            leftt = lauda(root.left,minn,root.val)
            right = lauda(root.right,root.val,maxx)
            return leftt and right
        return lauda(root,float('-inf'), float('inf') )