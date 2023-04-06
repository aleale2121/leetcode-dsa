# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, minSoFar=-math.inf, maxSoFar=math.inf):
            if not root:
                return True
            if root.val<=minSoFar or root.val>=maxSoFar:
                return False
            leftIsValid=isValid(root.left,minSoFar,root.val)
            rightIsValid=isValid(root.right,root.val,maxSoFar)
            return leftIsValid and rightIsValid 
        return isValid(root)